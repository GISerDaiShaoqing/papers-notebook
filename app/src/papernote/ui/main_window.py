from __future__ import annotations

import os
import re
import sys
from pathlib import Path

from PySide6.QtCore import QEasingCurve, QPropertyAnimation, QRect, QTimer, Qt, QUrl
from PySide6.QtGui import QAction, QDesktopServices, QFontDatabase, QIcon, QKeySequence, QTextCursor
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QSplitter,
    QTextBrowser,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from .ai_assistant import AIAssistantDrawer, AISettingsDialog, AIWorker, load_preferences
from .about_dialog import AboutDialog
from .pdf_reader import PDFReaderDialog
from .. import APP_DISPLAY_NAME, APP_NAME, APP_TAGLINE, __version__
from ..config import ProjectPaths
from ..resources import bundled_asset
from ..services.index_service import IndividualNote, load_categories, save_categories, scan_individual_notes
from ..services.markdown_service import read_text, render_html, write_text
from ..services.note_migration import slugify
from ..services.template_service import new_note_template
from .theme import apply_theme


class MainWindow(QMainWindow):
    """Modern, cross-platform Markdown editor for the paper notebook."""

    def __init__(self, paths: ProjectPaths) -> None:
        super().__init__()
        self.paths = paths
        self.current_file: Path | None = None
        self.current_pdf: PDFReaderDialog | None = None
        self.last_pdf_selection = ""
        self.ai_worker: AIWorker | None = None
        self.ai_history: list[dict[str, str]] = []
        self._drawer_open = False
        self.saved_text = ""
        self.notes: list[IndividualNote] = []

        self.setWindowTitle(f"{APP_DISPLAY_NAME}[*]")
        self.setWindowModified(False)
        self._set_initial_size()
        self._set_icon()
        self._build_menus()
        self._build_ui()
        self._build_ai_drawer()
        self.refresh_notes()

    def _set_initial_size(self) -> None:
        screen = QApplication.primaryScreen()
        available = screen.availableGeometry() if screen else None
        if available:
            width = min(1360, max(900, int(available.width() * 0.90)))
            height = min(840, max(600, int(available.height() * 0.88)))
            self.resize(width, height)
            self.move(available.center() - self.rect().center())
        else:
            self.resize(1200, 760)
        self.setMinimumSize(820, 580)

    def _set_icon(self) -> None:
        icon_path = self.paths.assets / "papernote.png"
        if not icon_path.is_file():
            icon_path = bundled_asset("papernote.png")
        if icon_path.is_file():
            self.setWindowIcon(QIcon(str(icon_path)))

    def _build_menus(self) -> None:
        file_menu = self.menuBar().addMenu("文件")
        self.new_action = QAction("新建笔记", self)
        self.new_action.setShortcut(QKeySequence.StandardKey.New)
        self.new_action.triggered.connect(lambda: self.new_note())
        file_menu.addAction(self.new_action)

        self.open_action = QAction("打开 Markdown…", self)
        self.open_action.setShortcut(QKeySequence.StandardKey.Open)
        self.open_action.triggered.connect(lambda: self.open_file())
        file_menu.addAction(self.open_action)

        self.save_action = QAction("保存", self)
        self.save_action.setShortcut(QKeySequence.StandardKey.Save)
        self.save_action.triggered.connect(lambda: self.save_file())
        file_menu.addAction(self.save_action)

        self.save_as_action = QAction("另存为…", self)
        self.save_as_action.setShortcut(QKeySequence("Ctrl+Shift+S"))
        self.save_as_action.triggered.connect(lambda: self.save_as())
        file_menu.addAction(self.save_as_action)

        file_menu.addSeparator()
        exit_action = QAction("退出", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        edit_menu = self.menuBar().addMenu("编辑")
        self.undo_action = QAction("撤销", self)
        self.undo_action.setShortcut(QKeySequence.StandardKey.Undo)
        self.undo_action.triggered.connect(lambda: self.editor.undo())
        edit_menu.addAction(self.undo_action)
        self.redo_action = QAction("重做", self)
        self.redo_action.setShortcut(QKeySequence.StandardKey.Redo)
        self.redo_action.triggered.connect(lambda: self.editor.redo())
        edit_menu.addAction(self.redo_action)

        help_menu = self.menuBar().addMenu("帮助")
        about_action = QAction(f"关于 {APP_NAME}", self)
        about_action.triggered.connect(lambda: AboutDialog(self).exec())
        help_menu.addAction(about_action)

    def _build_ui(self) -> None:
        central = QWidget(self)
        central_layout = QVBoxLayout(central)
        central_layout.setContentsMargins(0, 0, 0, 0)
        central_layout.setSpacing(0)

        header = QFrame()
        header.setObjectName("topHeader")
        header.setFixedHeight(72)
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(22, 10, 22, 10)
        header_layout.setSpacing(12)

        brand = QVBoxLayout()
        brand.setSpacing(1)
        brand_title = QLabel(APP_NAME)
        brand_title.setObjectName("brandMark")
        brand_subtitle = QLabel(APP_TAGLINE)
        brand_subtitle.setObjectName("brandSubtitle")
        brand.addWidget(brand_title)
        brand.addWidget(brand_subtitle)
        header_layout.addLayout(brand)
        header_layout.addStretch(1)

        self.new_button = QPushButton("＋  新建笔记")
        self.new_button.setObjectName("primaryButton")
        self.new_button.clicked.connect(lambda: self.new_note())
        header_layout.addWidget(self.new_button)

        self.publisher_button = QPushButton("出版社原文")
        self.publisher_button.setEnabled(False)
        self.publisher_button.clicked.connect(self.open_publisher)
        header_layout.addWidget(self.publisher_button)

        self.pdf_button = QPushButton("PDF 阅读")
        self.pdf_button.clicked.connect(self.open_pdf)
        header_layout.addWidget(self.pdf_button)

        self.ai_button = QPushButton("AI 助手")
        self.ai_button.clicked.connect(self.toggle_ai_drawer)
        header_layout.addWidget(self.ai_button)

        self.save_button = QPushButton("保存")
        self.save_button.setObjectName("primaryButton")
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(lambda: self.save_file())
        header_layout.addWidget(self.save_button)

        central_layout.addWidget(header)

        main_splitter = QSplitter(Qt.Orientation.Horizontal)
        main_splitter.setChildrenCollapsible(False)
        main_splitter.setHandleWidth(6)

        sidebar = QWidget()
        sidebar.setObjectName("sidebarPanel")
        sidebar.setMinimumWidth(205)
        side_layout = QVBoxLayout(sidebar)
        side_layout.setContentsMargins(17, 20, 13, 16)
        side_layout.setSpacing(10)

        eyebrow = QLabel("LIBRARY")
        eyebrow.setObjectName("sectionEyebrow")
        title_row = QHBoxLayout()
        title = QLabel("我的笔记")
        title.setObjectName("sidebarTitle")
        self.note_count = QLabel("0 篇")
        self.note_count.setObjectName("noteCount")
        title_row.addWidget(title)
        title_row.addStretch(1)
        title_row.addWidget(self.note_count)

        self.search_box = QLineEdit()
        self.search_box.setObjectName("searchBox")
        self.search_box.setPlaceholderText("搜索标题或分类…")
        self.search_box.textChanged.connect(self.refresh_notes)

        self.note_tree = QTreeWidget()
        self.note_tree.setObjectName("noteTree")
        self.note_tree.setHeaderHidden(True)
        self.note_tree.setIndentation(15)
        self.note_tree.setAnimated(True)
        self.note_tree.itemClicked.connect(self._tree_selected)

        side_layout.addWidget(eyebrow)
        side_layout.addLayout(title_row)
        side_layout.addWidget(self.search_box)
        side_layout.addWidget(self.note_tree, 1)
        main_splitter.addWidget(sidebar)

        self.workspace_splitter = QSplitter(Qt.Orientation.Horizontal)
        self.workspace_splitter.setChildrenCollapsible(False)
        self.workspace_splitter.setHandleWidth(6)
        self.workspace_splitter.addWidget(self._build_editor_panel())
        self.workspace_splitter.addWidget(self._build_preview_panel())
        main_splitter.addWidget(self.workspace_splitter)
        main_splitter.setStretchFactor(0, 0)
        main_splitter.setStretchFactor(1, 1)
        main_splitter.setSizes([260, max(600, self.width() - 260)])
        self.workspace_splitter.setStretchFactor(0, 1)
        self.workspace_splitter.setStretchFactor(1, 1)
        self.workspace_splitter.setSizes([540, 540])
        central_layout.addWidget(main_splitter, 1)

        self.setCentralWidget(central)
        self.statusBar().showMessage("准备就绪")

    def _build_ai_drawer(self) -> None:
        self.ai_drawer = AIAssistantDrawer(self)
        self.ai_drawer.configure.connect(self.configure_ai)
        self.ai_drawer.request.connect(self._start_ai_request)
        self.ai_drawer.translate_selection.connect(self.translate_selected_text)
        self.ai_drawer.read_paper.connect(self._read_current_pdf)
        self.ai_drawer.clear_requested.connect(self._clear_ai_history)
        self.ai_drawer.close_requested.connect(self.close_ai_drawer)
        self.ai_drawer.hide()
        self.drawer_animation = QPropertyAnimation(self.ai_drawer, b"geometry", self)
        self.drawer_animation.setDuration(180)
        self.drawer_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.drawer_animation.finished.connect(self._drawer_animation_finished)

    def _drawer_rect(self) -> QRect:
        central = self.centralWidget()
        top_left = central.mapTo(self, central.rect().topLeft())
        top = top_left.y() + 72
        width = min(440, max(340, self.width() // 3))
        height = max(280, central.height() - 72)
        return QRect(self.width() - width - 8, top, width, height)

    def toggle_ai_drawer(self) -> None:
        if self._drawer_open:
            self.close_ai_drawer()
            return
        self._drawer_open = True
        target = self._drawer_rect()
        start = QRect(target)
        start.moveLeft(self.width())
        self.ai_drawer.setGeometry(start)
        self.ai_drawer.show()
        self.ai_drawer.raise_()
        self.drawer_animation.stop()
        self.drawer_animation.setStartValue(start)
        self.drawer_animation.setEndValue(target)
        self.drawer_animation.start()

    def close_ai_drawer(self) -> None:
        if not self._drawer_open or not self.ai_drawer.isVisible():
            return
        self._drawer_open = False
        start = self.ai_drawer.geometry()
        end = QRect(start)
        end.moveLeft(self.width())
        self.drawer_animation.stop()
        self.drawer_animation.setStartValue(start)
        self.drawer_animation.setEndValue(end)
        self.drawer_animation.start()

    def _drawer_animation_finished(self) -> None:
        if not self._drawer_open:
            self.ai_drawer.hide()

    def configure_ai(self) -> None:
        dialog = AISettingsDialog(self)
        if dialog.exec() == AISettingsDialog.DialogCode.Accepted:
            self.statusBar().showMessage("AI 模型配置已保存")

    def _start_ai_request(self, prompt: str, context: str, mode: str) -> None:
        if self.ai_worker and self.ai_worker.isRunning():
            return
        preferences = load_preferences()
        if not preferences.base_url or not preferences.model:
            self.configure_ai()
            preferences = load_preferences()
        if not preferences.base_url or not preferences.model:
            return
        local_endpoint = "localhost" in preferences.base_url or "127.0.0.1" in preferences.base_url
        if not preferences.api_key and not local_endpoint:
            QMessageBox.information(self, "需要 API 密钥", "请先在 AI 助手设置中配置 API 密钥。")
            self.configure_ai()
            preferences = load_preferences()
            if not preferences.api_key and "localhost" not in preferences.base_url and "127.0.0.1" not in preferences.base_url:
                return

        self.ai_drawer.add_message("user", prompt)
        self.ai_drawer.set_busy(True)
        self.ai_drawer.set_progress("正在连接模型服务…")
        history = self.ai_history[-12:] if mode == "chat" else []
        worker = AIWorker(preferences, prompt, context, mode, history)
        worker.setParent(self)
        worker.completed.connect(self._ai_completed)
        worker.failed.connect(self._ai_failed)
        worker.progress.connect(self.ai_drawer.set_progress)
        worker.finished.connect(self._ai_worker_finished)
        worker.finished.connect(worker.deleteLater)
        self.ai_worker = worker
        worker.start()

    def _ai_completed(self, text: str) -> None:
        worker = self.ai_worker
        if worker and worker.mode == "paper":
            self.ai_history = [
                {"role": "user", "content": worker.prompt},
                {"role": "assistant", "content": text},
            ]
        elif worker and worker.mode == "chat":
            self.ai_history.extend(
                [
                    {"role": "user", "content": worker.prompt},
                    {"role": "assistant", "content": text},
                ]
            )
            self.ai_history = self.ai_history[-12:]
        self.ai_drawer.add_message("assistant", text)
        self.statusBar().showMessage("AI 回复完成")

    def _ai_failed(self, message: str) -> None:
        self.ai_drawer.add_message("assistant", f"请求失败：{message}")
        self.statusBar().showMessage("AI 请求失败")

    def _ai_worker_finished(self) -> None:
        self.ai_drawer.set_busy(False)
        self.ai_worker = None

    def _clear_ai_history(self) -> None:
        self.ai_history.clear()

    def _request_translation(self, text: str) -> None:
        if not text.strip():
            QMessageBox.information(self, "没有选中文字", "请先在笔记或 PDF 中选择要翻译的内容。")
            return
        if not self._drawer_open:
            self.toggle_ai_drawer()
        self._start_ai_request("请翻译选中文字。", text, "translate")

    def translate_selected_text(self) -> None:
        selected = self.editor.textCursor().selectedText().replace("\u2029", "\n")
        self._request_translation(selected or self.last_pdf_selection)

    def translate_text_with_ai(self, text: str) -> None:
        self.last_pdf_selection = text
        self._request_translation(text)

    def read_text_with_ai(self, text: str, title: str = "当前 PDF") -> None:
        if not self._drawer_open:
            self.toggle_ai_drawer()
        self._start_ai_request(
            f"请按精读笔记结构分析《{title}》：说明研究问题、研究空白、数据和尺度、方法与假设、主要结果及证据、关键图表、局限与不确定性，并提出后续问题。请标注页码，不要补造 PDF 未提供的信息。",
            text,
            "paper",
        )

    def _read_current_pdf(self) -> None:
        if not self.current_pdf:
            QMessageBox.information(self, "没有打开 PDF", "请先打开本地 PDF，再使用精读功能。")
            return
        try:
            text = self.current_pdf.document_text()
        except Exception as exc:
            QMessageBox.critical(self, "读取 PDF 失败", str(exc))
            return
        self.read_text_with_ai(text, self.current_pdf.pdf_path.name)

    def open_publisher(self) -> None:
        if not self.current_file:
            QMessageBox.information(self, "没有打开笔记", "先从左侧选择一篇论文笔记。")
            return
        text = self.editor.toPlainText()
        doi = ""
        for line in text.splitlines():
            match = re.match(r"^\s*(?:-\s*)?doi\s*:\s*(.*?)\s*$", line, re.IGNORECASE)
            if match:
                doi = match.group(1).strip().strip("`<>[]() ")
                break
        doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi, flags=re.IGNORECASE)
        if doi:
            QDesktopServices.openUrl(QUrl(f"https://doi.org/{doi}"))
            return

        link_match = re.search(r"(?:Link|URL)\s*:\s*.*?\((https?://[^)]+)\)", text, re.IGNORECASE)
        if link_match:
            QDesktopServices.openUrl(QUrl(link_match.group(1)))
            return
        QMessageBox.information(self, "没有原文链接", "这篇笔记没有填写 DOI 或出版商链接。")

    def open_pdf(self) -> None:
        if self.current_pdf:
            self.current_pdf.show()
            self.current_pdf.raise_()
            self.current_pdf.activateWindow()
            return
        start = self.current_file.parent if self.current_file else self.paths.repository
        filename, _ = QFileDialog.getOpenFileName(self, "打开本地 PDF", str(start), "PDF 文件 (*.pdf)")
        if not filename:
            return
        try:
            reader = PDFReaderDialog(Path(filename), self)
        except Exception as exc:
            QMessageBox.critical(self, "无法打开 PDF", str(exc))
            return
        reader.setWindowIcon(self.windowIcon())
        reader.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        reader.page_view.selection_changed.connect(self._set_pdf_selection)
        reader.destroyed.connect(self._pdf_reader_closed)
        self.current_pdf = reader
        reader.show()

    def _set_pdf_selection(self, text: str) -> None:
        self.last_pdf_selection = text

    def _pdf_reader_closed(self, _object=None) -> None:
        self.current_pdf = None
        self.last_pdf_selection = ""

    def paste_pdf_text(self, text: str) -> None:
        self.show()
        self.raise_()
        self.activateWindow()
        self.editor.setFocus()
        cursor = self.editor.textCursor()
        cursor.insertText(text)
        self.editor.setTextCursor(cursor)
        self.statusBar().showMessage("已将 PDF 选区粘贴到笔记")

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        if hasattr(self, "ai_drawer") and self.ai_drawer.isVisible() and self._drawer_open:
            self.ai_drawer.setGeometry(self._drawer_rect())

    def _build_editor_panel(self) -> QFrame:
        panel = QFrame()
        panel.setObjectName("paneCard")
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        toolbar = QHBoxLayout()
        toolbar.setContentsMargins(18, 14, 18, 12)
        toolbar.addWidget(self._pane_heading("MARKDOWN", "自由编辑笔记内容"))
        toolbar.addStretch(1)
        self.file_label = QLabel("未打开笔记")
        self.file_label.setObjectName("paneHint")
        toolbar.addWidget(self.file_label)
        layout.addLayout(toolbar)

        self.editor = QPlainTextEdit()
        self.editor.setObjectName("noteEditor")
        fixed_font = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        fixed_font.setPointSize(11)
        self.editor.setFont(fixed_font)
        self.editor.setPlaceholderText("从左侧选择一篇笔记，或新建一篇开始记录。")
        self.editor.textChanged.connect(self._on_editor_changed)
        layout.addWidget(self.editor, 1)
        return panel

    def _build_preview_panel(self) -> QFrame:
        panel = QFrame()
        panel.setObjectName("paneCard")
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        toolbar = QHBoxLayout()
        toolbar.setContentsMargins(18, 14, 18, 12)
        toolbar.addWidget(self._pane_heading("PREVIEW", "排版实时更新"))
        toolbar.addStretch(1)
        self.preview_hint = QLabel("长文阅读排版")
        self.preview_hint.setObjectName("paneHint")
        toolbar.addWidget(self.preview_hint)
        layout.addLayout(toolbar)

        self.preview = QTextBrowser()
        self.preview.setObjectName("notePreview")
        self.preview.setOpenExternalLinks(True)
        self.preview.setOpenLinks(True)
        layout.addWidget(self.preview, 1)
        self.preview_timer = QTimer(self)
        self.preview_timer.setSingleShot(True)
        self.preview_timer.setInterval(220)
        self.preview_timer.timeout.connect(self._update_preview)
        return panel

    @staticmethod
    def _pane_heading(eyebrow_text: str, title_text: str) -> QWidget:
        heading = QWidget()
        layout = QVBoxLayout(heading)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        eyebrow = QLabel(eyebrow_text)
        eyebrow.setObjectName("sectionEyebrow")
        title = QLabel(title_text)
        title.setObjectName("paneTitle")
        layout.addWidget(eyebrow)
        layout.addWidget(title)
        return heading

    def refresh_notes(self, _query: str = "") -> None:
        query = self.search_box.text().strip().casefold() if hasattr(self, "search_box") else ""
        self.notes = scan_individual_notes(self.paths.repository / "notes")
        visible = [note for note in self.notes if query in note.title.casefold() or query in note.category.casefold()]
        self.note_tree.clear()

        categories: dict[str, QTreeWidgetItem] = {}
        selected_item = None
        notes_root = self.paths.repository / "notes"
        category_names = set(load_categories(notes_root))
        category_names.update(note.category for note in self.notes if note.category)
        category_names.update(note.category or "未分类" for note in visible)
        for category in sorted(category_names, key=str.casefold):
            if query and query not in category.casefold() and not any(note.category == category for note in visible):
                continue
            category_item = QTreeWidgetItem([category])
            category_item.setFlags(category_item.flags() & ~Qt.ItemFlag.ItemIsSelectable)
            self.note_tree.addTopLevelItem(category_item)
            category_item.setExpanded(True)
            categories[category] = category_item

        for note in visible:
            category = note.category or "未分类"
            item = QTreeWidgetItem([note.title])
            item.setData(0, Qt.ItemDataRole.UserRole, str(note.path))
            categories[category].addChild(item)
            if self.current_file and note.path.resolve() == self.current_file.resolve():
                selected_item = item

        if selected_item:
            self.note_tree.setCurrentItem(selected_item)
        self.note_count.setText(f"{len(self.notes)} 篇")
        self.statusBar().showMessage(f"共 {len(self.notes)} 篇笔记")

    def _tree_selected(self, item: QTreeWidgetItem, _column: int) -> None:
        path_value = item.data(0, Qt.ItemDataRole.UserRole)
        if path_value:
            self.open_note(Path(path_value))

    def open_note(self, path: Path) -> None:
        if not self._confirm_unsaved_changes():
            return
        path = path.expanduser().resolve()
        try:
            text = read_text(path)
        except OSError as exc:
            QMessageBox.critical(self, "无法打开笔记", str(exc))
            return

        self.current_file = path
        self.publisher_button.setEnabled(True)
        self.editor.blockSignals(True)
        self.editor.setPlainText(text)
        self.editor.blockSignals(False)
        self.saved_text = text
        self.file_label.setText(path.name)
        self._set_modified(False)
        self._update_preview()
        self.statusBar().showMessage(f"已打开：{self._display_path(path)}")

    def open_file(self) -> None:
        if not self._confirm_unsaved_changes():
            return
        start = self.current_file.parent if self.current_file else self.paths.repository / "notes"
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "打开 Markdown 笔记",
            str(start),
            "Markdown 文件 (*.md *.markdown);;所有文件 (*.*)",
        )
        if filename:
            self.open_note(Path(filename))

    def save_file(self) -> None:
        if self.current_file is None:
            self.save_as()
            return
        try:
            text = self.editor.toPlainText()
            write_text(self.current_file, text)
        except OSError as exc:
            QMessageBox.critical(self, "无法保存笔记", str(exc))
            return
        self.saved_text = text
        self._set_modified(False)
        self.refresh_notes()
        self.statusBar().showMessage(f"已保存：{self._display_path(self.current_file)}")

    def save_as(self) -> None:
        start = self.current_file or self.paths.repository / "notes" / "新笔记.md"
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "另存为 Markdown 笔记",
            str(start),
            "Markdown 文件 (*.md)",
        )
        if not filename:
            return
        self.current_file = Path(filename).expanduser().resolve()
        self.file_label.setText(self.current_file.name)
        self.publisher_button.setEnabled(True)
        self.save_file()

    def new_note(self) -> None:
        if not self._confirm_unsaved_changes():
            return
        title, accepted = QInputDialog.getText(self, "新建笔记", "论文标题：")
        title = title.strip()
        if not accepted or not title:
            return

        notes_root = self.paths.repository / "notes"
        categories = load_categories(notes_root)
        categories.extend(note.category for note in self.notes if note.category not in categories)
        category, accepted = QInputDialog.getItem(
            self,
            "选择分类",
            "分类名称：",
            categories,
            0,
            True,
        )
        category = category.strip()
        if not accepted or not category:
            return

        directory = self.paths.repository / "notes" / slugify(category)
        path = directory / f"{slugify(title)}.md"
        if path.exists():
            QMessageBox.warning(self, "无法新建", f"同名笔记已存在：\n{path}")
            return
        write_text(path, new_note_template(title, category))
        if category.casefold() not in {item.casefold() for item in categories}:
            save_categories(notes_root, [*categories, category])
        self.refresh_notes()
        self.open_note(path)
        self.editor.moveCursor(QTextCursor.MoveOperation.End)
        self.editor.setFocus()

    def _on_editor_changed(self) -> None:
        self._set_modified(self.editor.toPlainText() != self.saved_text)
        self.preview_timer.start()

    def _set_modified(self, modified: bool) -> None:
        self.setWindowModified(modified)
        self.save_button.setEnabled(modified or self.current_file is None)
        if self.current_file:
            self.file_label.setText(f"{self.current_file.name}{'  •' if modified else ''}")
        elif modified:
            self.file_label.setText("未保存笔记  •")
        else:
            self.file_label.setText("未打开笔记")

    def _update_preview(self) -> None:
        base_directory = self.current_file.parent if self.current_file else self.paths.repository / "notes"
        base_url = QUrl.fromLocalFile(str(base_directory.resolve()) + os.sep)
        self.preview.document().setBaseUrl(base_url)
        self.preview.setHtml(render_html(self.editor.toPlainText()))

    def _confirm_unsaved_changes(self) -> bool:
        if self.editor.toPlainText() == self.saved_text:
            return True
        box = QMessageBox(self)
        box.setWindowTitle("笔记尚未保存")
        box.setText("当前笔记有未保存的修改。")
        box.setInformativeText("保存修改后再继续吗？")
        box.setIcon(QMessageBox.Icon.Warning)
        save = box.addButton("保存", QMessageBox.ButtonRole.AcceptRole)
        box.addButton("不保存", QMessageBox.ButtonRole.DestructiveRole)
        box.addButton("取消", QMessageBox.ButtonRole.RejectRole)
        box.setDefaultButton(save)
        box.exec()
        clicked = box.clickedButton()
        if clicked is save:
            self.save_file()
            return self.editor.toPlainText() == self.saved_text
        if clicked is not None and clicked.text() == "不保存":
            self.editor.blockSignals(True)
            self.editor.setPlainText(self.saved_text)
            self.editor.blockSignals(False)
            self._set_modified(False)
            self._update_preview()
            return True
        return False

    def _display_path(self, path: Path) -> str:
        try:
            return path.relative_to(self.paths.repository).as_posix()
        except ValueError:
            return str(path)

    def closeEvent(self, event) -> None:
        if self.ai_worker and self.ai_worker.isRunning():
            QMessageBox.information(self, "AI 正在处理", "等当前模型请求完成后再关闭程序。")
            event.ignore()
            return
        if self._confirm_unsaved_changes():
            event.accept()
        else:
            event.ignore()


def run_gui(repository: Path | None = None) -> None:
    app = QApplication.instance() or QApplication(sys.argv)
    app.setApplicationName("PaperNote")
    app.setOrganizationName("PaperNote")
    app.setApplicationDisplayName(APP_DISPLAY_NAME)
    app.setApplicationVersion(__version__)
    apply_theme(app)

    resolved_repository = repository
    if resolved_repository is None:
        selected = QFileDialog.getExistingDirectory(
            None,
            "选择 papers-notebook 仓库文件夹",
            str(Path.home()),
        )
        if not selected:
            return
        resolved_repository = Path(selected)

    try:
        paths = ProjectPaths.from_root(resolved_repository)
    except FileNotFoundError:
        QMessageBox.critical(None, "不是笔记仓库", "所选文件夹中没有 README.md，请重新选择 papers-notebook 仓库根目录。")
        return

    icon_path = paths.assets / "papernote.png"
    if not icon_path.is_file():
        icon_path = bundled_asset("papernote.png")
    if icon_path.is_file():
        app.setWindowIcon(QIcon(str(icon_path)))

    window = MainWindow(paths)
    window.show()
    app.exec()
