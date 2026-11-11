from __future__ import annotations

import html
import re

from PySide6.QtCore import QSettings, Qt, QThread, Signal
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QPlainTextEdit,
    QTextBrowser,
    QVBoxLayout,
)

from .. import APP_NAME
from ..services.llm_service import LLMPreferences, LLMRequestError, complete_chat


PROVIDER_PRESETS = (
    ("自定义兼容接口", "", ""),
    ("OpenAI", "https://api.openai.com/v1", "gpt-4o-mini"),
    ("DeepSeek", "https://api.deepseek.com/v1", "deepseek-chat"),
    ("通义千问", "https://dashscope.aliyuncs.com/compatible-mode/v1", "qwen-plus"),
    ("Kimi", "https://api.moonshot.cn/v1", "kimi-k2-turbo-preview"),
    ("智谱 GLM", "https://open.bigmodel.cn/api/paas/v4", "glm-4-flash"),
    ("Ollama（本地）", "http://localhost:11434/v1", "qwen2.5:7b"),
)

KEYRING_SERVICE = "PaperNote"
KEYRING_USER = "openai-compatible"


def load_preferences() -> LLMPreferences:
    settings = QSettings("PaperNote", "PaperNote")
    try:
        import keyring

        api_key = keyring.get_password(KEYRING_SERVICE, KEYRING_USER) or ""
    except Exception:
        api_key = ""
    return LLMPreferences(
        base_url=str(settings.value("ai/base_url", "https://api.openai.com/v1")),
        model=str(settings.value("ai/model", "gpt-4o-mini")),
        api_key=api_key,
    )


class AISettingsDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("AI 助手设置")
        self.setMinimumWidth(460)
        self._preferences = load_preferences()

        layout = QVBoxLayout(self)
        intro = QLabel("配置兼容 OpenAI Chat Completions 接口的模型服务。Ollama 等本地服务可不填密钥。")
        intro.setWordWrap(True)
        intro.setObjectName("paneHint")
        layout.addWidget(intro)

        form = QFormLayout()
        self.provider_combo = QComboBox()
        for label, _url, _model in PROVIDER_PRESETS:
            self.provider_combo.addItem(label)
        self.base_url = QLineEdit(self._preferences.base_url)
        self.base_url.setPlaceholderText("https://api.example.com/v1")
        self.model = QLineEdit(self._preferences.model)
        self.model.setPlaceholderText("模型 ID，例如 gpt-4o-mini")
        self.api_key = QLineEdit()
        self.api_key.setEchoMode(QLineEdit.EchoMode.Password)
        self.api_key.setPlaceholderText("密钥保存在系统钥匙串；留空则不修改")
        self.clear_key = QCheckBox("清除已保存的密钥")
        form.addRow("服务商", self.provider_combo)
        form.addRow("API 地址", self.base_url)
        form.addRow("模型", self.model)
        form.addRow("API 密钥", self.api_key)
        form.addRow("", self.clear_key)
        layout.addLayout(form)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self._save)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        self.provider_combo.currentIndexChanged.connect(self._apply_preset)

    def _apply_preset(self, index: int) -> None:
        _label, url, model = PROVIDER_PRESETS[index]
        if url:
            self.base_url.setText(url)
        if model:
            self.model.setText(model)

    def _save(self) -> None:
        base_url = self.base_url.text().strip()
        model = self.model.text().strip()
        if not base_url or not model:
            QMessageBox.warning(self, "信息不完整", "请填写 API 地址和模型名称。")
            return
        try:
            import keyring

            if self.clear_key.isChecked():
                try:
                    keyring.delete_password(KEYRING_SERVICE, KEYRING_USER)
                except keyring.errors.PasswordDeleteError:
                    pass
            elif self.api_key.text().strip():
                keyring.set_password(KEYRING_SERVICE, KEYRING_USER, self.api_key.text().strip())
        except Exception as exc:
            if self.api_key.text().strip() or self.clear_key.isChecked():
                QMessageBox.critical(
                    self,
                    "无法访问系统钥匙串",
                    "API 密钥没有保存。请检查当前系统的钥匙串/凭据存储设置后重试。\n\n"
                    f"{exc}",
                )
                return

        settings = QSettings("PaperNote", "PaperNote")
        settings.setValue("ai/base_url", base_url)
        settings.setValue("ai/model", model)
        settings.sync()
        self.accept()


class AIWorker(QThread):
    completed = Signal(str)
    failed = Signal(str)
    progress = Signal(str)

    def __init__(
        self,
        preferences: LLMPreferences,
        prompt: str,
        context: str,
        mode: str,
        history: list[dict[str, str]] | None = None,
    ) -> None:
        super().__init__()
        self.preferences = preferences
        self.prompt = prompt
        self.context = context
        self.mode = mode
        self.history = history or []

    @staticmethod
    def _chunks(text: str, limit: int = 10000) -> list[str]:
        paragraphs = re.split(r"(?<=\n)", text)
        chunks: list[str] = []
        current = ""
        for paragraph in paragraphs:
            if current and len(current) + len(paragraph) > limit:
                chunks.append(current)
                current = ""
            if len(paragraph) > limit:
                if current:
                    chunks.append(current)
                    current = ""
                chunks.extend(paragraph[index : index + limit] for index in range(0, len(paragraph), limit))
            else:
                current += paragraph
        if current:
            chunks.append(current)
        return chunks

    def run(self) -> None:
        try:
            if self.mode == "translate":
                result = complete_chat(
                    self.preferences,
                    [
                        {
                            "role": "system",
                            "content": (
                                "准确翻译用户提供的选区。英文翻译为简体中文，中文翻译为英文。"
                                "保留专业术语、缩写、公式和引文，不补写原文没有的信息。"
                            ),
                        },
                        {"role": "user", "content": f"{self.prompt}\n\n待翻译内容：\n{self.context}"},
                    ],
                )
            elif self.mode == "paper":
                result = self._read_paper()
            else:
                messages = [
                    {
                        "role": "system",
                        "content": "你是严谨的论文阅读助手。依据用户提供的材料回答；区分原文结论和推断，信息不足时明确说明。",
                    },
                    *self.history,
                ]
                if self.context:
                    messages.append({"role": "user", "content": f"参考材料：\n{self.context}"})
                messages.append({"role": "user", "content": self.prompt})
                result = complete_chat(self.preferences, messages)
            self.completed.emit(result)
        except LLMRequestError as exc:
            self.failed.emit(str(exc))
        except Exception as exc:
            self.failed.emit(f"AI 请求失败：{exc}")

    def _read_paper(self) -> str:
        if not self.context.strip():
            raise LLMRequestError("当前 PDF 没有可提取的文字，请检查它是否为扫描图片。")
        if len(self.context) > 300000:
            raise LLMRequestError("PDF 可提取文字超过 300,000 字符；请拆分论文或先选择需要阅读的部分。")
        chunks = self._chunks(self.context)
        summaries: list[str] = []
        for index, chunk in enumerate(chunks, start=1):
            self.progress.emit(f"正在阅读 PDF：第 {index}/{len(chunks)} 部分")
            summaries.append(
                complete_chat(
                    self.preferences,
                    [
                        {
                            "role": "system",
                            "content": (
                                "阅读论文片段并用中文提取可核对的信息：研究问题、数据与尺度、方法、结果、"
                                "作者提到的局限。保留原文页码标记；不在片段中出现的信息写‘本段未提及’。"
                            ),
                        },
                        {"role": "user", "content": f"片段 {index}/{len(chunks)}：\n{chunk}"},
                    ],
                )
            )

        self.progress.emit("正在整理整篇论文的论证脉络…")
        synthesis = "\n\n".join(f"片段 {index}:\n{text}" for index, text in enumerate(summaries, start=1))
        return complete_chat(
            self.preferences,
            [
                {
                    "role": "system",
                    "content": (
                        "你是严谨的论文精读助手，只依据提供的 PDF 内容作答；缺少证据时明确写出，不要猜测。"
                        "使用中文，保留必要的英文专业术语，并按以下笔记范例的栏目组织草稿："
                        "Notes、Highlights、Research gap/question、Discussion/Conclusion、"
                        "Graph/Table interested、Resources。Notes 中解释问题、数据、方法和主要结果；"
                        "图表部分说明图表展示什么以及它支持什么结论。保留页码线索，区分作者结论和归纳。"
                        "不要代写读者个人评价；可以列出供读者自己补充的问题。"
                    ),
                },
                {
                    "role": "user",
                    "content": f"用户关注点：{self.prompt}\n\n按片段整理的论文信息：\n{synthesis}",
                },
            ],
        )


class AIAssistantDrawer(QFrame):
    request = Signal(str, str, str)
    configure = Signal()
    translate_selection = Signal()
    read_paper = Signal()
    clear_requested = Signal()
    close_requested = Signal()

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("aiDrawer")
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setMinimumWidth(360)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 15, 16, 16)
        layout.setSpacing(10)

        header = QHBoxLayout()
        title = QLabel("AI 助手")
        title.setObjectName("sidebarTitle")
        settings_button = QPushButton("设置")
        settings_button.clicked.connect(self.configure.emit)
        close_button = QPushButton("收起")
        close_button.clicked.connect(self.close_requested.emit)
        header.addWidget(title)
        header.addStretch(1)
        header.addWidget(settings_button)
        header.addWidget(close_button)
        layout.addLayout(header)

        privacy = QLabel("仅在点击发送后，选区或 PDF 文本才会发送到你配置的模型服务。")
        privacy.setObjectName("paneHint")
        privacy.setWordWrap(True)
        layout.addWidget(privacy)

        actions = QHBoxLayout()
        self.translate_button = QPushButton("翻译选中文字")
        self.translate_button.clicked.connect(self.translate_selection.emit)
        self.read_button = QPushButton("精读当前 PDF")
        self.read_button.clicked.connect(self.read_paper.emit)
        actions.addWidget(self.translate_button)
        actions.addWidget(self.read_button)
        self.clear_button = QPushButton("清空对话")
        self.clear_button.clicked.connect(self._clear_chat)
        actions.addWidget(self.clear_button)
        layout.addLayout(actions)

        self.chat = QTextBrowser()
        self.chat.setOpenExternalLinks(True)
        self.chat.append(
            "<p style='color:#71828a'>可以翻译当前选区、精读已打开的 PDF，或在下方输入问题。使用前请在“设置”中填写模型服务。</p>"
        )
        layout.addWidget(self.chat, 1)

        self.prompt = QPlainTextEdit()
        self.prompt.setMaximumHeight(96)
        self.prompt.setPlaceholderText("输入关于当前论文的问题…")
        layout.addWidget(self.prompt)
        self.send_button = QPushButton("发送")
        self.send_button.setObjectName("primaryButton")
        self.send_button.clicked.connect(self._send_prompt)
        layout.addWidget(self.send_button)

    def _send_prompt(self) -> None:
        prompt = self.prompt.toPlainText().strip()
        if prompt:
            self.prompt.clear()
            self.request.emit(prompt, "", "chat")

    def add_message(self, role: str, text: str) -> None:
        label = "你" if role == "user" else f"{APP_NAME} AI"
        color = "#2d6876" if role == "user" else "#445f68"
        safe_text = html.escape(text).replace("\n", "<br>")
        self.chat.append(
            f"<p style='margin:12px 0 3px;color:{color};font-weight:600'>{label}</p>"
            f"<p style='margin:0 0 12px;line-height:1.65'>{safe_text}</p>"
        )

    def set_busy(self, busy: bool) -> None:
        self.send_button.setEnabled(not busy)
        self.read_button.setEnabled(not busy)
        self.translate_button.setEnabled(not busy)
        self.prompt.setEnabled(not busy)
        self.send_button.setText("正在处理…" if busy else "发送")

    def set_progress(self, text: str) -> None:
        self.chat.append(f"<p style='color:#7a8b91'><i>{html.escape(text)}</i></p>")

    def clear_chat(self) -> None:
        self.chat.clear()
        self.chat.append(
            "<p style='color:#71828a'>可以翻译当前选区、精读已打开的 PDF，或在下方输入问题。使用前请在“设置”中填写模型服务。</p>"
        )

    def _clear_chat(self) -> None:
        self.clear_chat()
        self.clear_requested.emit()
