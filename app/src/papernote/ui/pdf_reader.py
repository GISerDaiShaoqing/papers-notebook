from __future__ import annotations

from pathlib import Path

import pypdfium2 as pdfium
from pypdf import PdfWriter
from pypdf.annotations import Highlight
from pypdf.generic import ArrayObject, FloatObject
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QBrush, QColor, QImage, QKeySequence, QPainter, QPen, QPixmap, QShortcut
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QFileDialog,
    QGraphicsScene,
    QGraphicsView,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class PDFPageView(QGraphicsView):
    selection_changed = Signal(str)
    highlight_selected = Signal(int, list, str)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setScene(QGraphicsScene(self))
        self.setRenderHints(QPainter.RenderHint.Antialiasing | QPainter.RenderHint.SmoothPixmapTransform)
        self.setBackgroundBrush(QColor("#e9eef0"))
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.setDragMode(QGraphicsView.DragMode.NoDrag)
        self.page = None
        self.text_page = None
        self.page_index = 0
        self.page_width = 0.0
        self.page_height = 0.0
        self.scale_factor = 1.0
        self.pixmap_width = 0
        self.pixmap_height = 0
        self._press_point = None
        self._selection_rect = None
        self._selection_item = None
        self._selected_quads: list[tuple[float, float, float, float]] = []
        self._selected_text = ""
        self._highlight_items = []

    @property
    def selected_text(self) -> str:
        return self._selected_text

    def set_page(self, page, text_page, page_index: int, scale_factor: float) -> None:
        self.page = page
        self.text_page = text_page
        self.page_index = page_index
        self.scale_factor = scale_factor
        self.page_width = float(page.get_width())
        self.page_height = float(page.get_height())

        bitmap = page.render(scale=scale_factor, rotation=0, rev_byteorder=True, prefer_bgrx=False)
        image = QImage(
            memoryview(bitmap.buffer),
            bitmap.width,
            bitmap.height,
            bitmap.stride,
            QImage.Format.Format_RGB888,
        ).copy()
        pixmap = QPixmap.fromImage(image)
        self.pixmap_width = pixmap.width()
        self.pixmap_height = pixmap.height()

        scene = self.scene()
        scene.clear()
        scene.setSceneRect(0, 0, self.pixmap_width, self.pixmap_height)
        scene.addPixmap(pixmap)
        self._selection_item = None
        self._highlight_items = []
        self._clear_selection()

    def _clear_selection(self) -> None:
        self._selection_rect = None
        self._selected_text = ""
        self._selected_quads = []
        self.selection_changed.emit("")

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton and self.page is not None:
            self._press_point = self.mapToScene(event.position().toPoint())
            self._selection_rect = None
            if self._selection_item:
                self.scene().removeItem(self._selection_item)
                self._selection_item = None
            event.accept()
            return
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event) -> None:
        if self._press_point is not None:
            end_point = self.mapToScene(event.position().toPoint())
            rect = self._bounded_rect(self._press_point, end_point)
            self._selection_rect = rect
            if self._selection_item:
                self.scene().removeItem(self._selection_item)
            self._selection_item = self.scene().addRect(
                rect,
                QPen(QColor("#3c8792"), 1.5),
                QBrush(QColor(107, 186, 192, 85)),
            )
            self._selection_item.setZValue(2)
            event.accept()
            return
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton and self._press_point is not None:
            self._press_point = None
            self._extract_selection()
            event.accept()
            return
        super().mouseReleaseEvent(event)

    def _bounded_rect(self, first, second):
        left = max(0.0, min(first.x(), second.x()))
        top = max(0.0, min(first.y(), second.y()))
        right = min(float(self.pixmap_width), max(first.x(), second.x()))
        bottom = min(float(self.pixmap_height), max(first.y(), second.y()))
        from PySide6.QtCore import QRectF

        return QRectF(left, top, max(0.0, right - left), max(0.0, bottom - top))

    def _extract_selection(self) -> None:
        rect = self._selection_rect
        if rect is None or rect.width() < 3 or rect.height() < 3 or self.text_page is None:
            self._clear_selection()
            return

        left = rect.left() / self.scale_factor
        right = rect.right() / self.scale_factor
        top = self.page_height - rect.top() / self.scale_factor
        bottom = self.page_height - rect.bottom() / self.scale_factor
        try:
            selected_text = self.text_page.get_text_bounded(left, bottom, right, top).strip()
        except Exception:
            selected_text = ""

        self._selected_text = selected_text
        self._selected_quads = self._quads_for_rect(rect)
        self.selection_changed.emit(selected_text)

    def _quads_for_rect(self, rect) -> list[tuple[float, float, float, float]]:
        if self.text_page is None:
            return []
        text = self.text_page.get_text_range()
        selection_left = rect.left() / self.scale_factor
        selection_right = rect.right() / self.scale_factor
        selection_top = self.page_height - rect.top() / self.scale_factor
        selection_bottom = self.page_height - rect.bottom() / self.scale_factor

        lines: list[dict[str, float]] = []
        for index, character in enumerate(text):
            if character.isspace():
                continue
            try:
                left, bottom, right, top = self.text_page.get_charbox(index)
            except Exception:
                continue
            if right <= left or top <= bottom:
                continue
            if right < selection_left or left > selection_right or top < selection_bottom or bottom > selection_top:
                continue
            center = (top + bottom) / 2
            line = next((item for item in lines if abs(item["center"] - center) <= 3.5), None)
            if line is None:
                line = {"center": center, "left": left, "right": right, "bottom": bottom, "top": top}
                lines.append(line)
            else:
                line["left"] = min(line["left"], left)
                line["right"] = max(line["right"], right)
                line["bottom"] = min(line["bottom"], bottom)
                line["top"] = max(line["top"], top)

        lines.sort(key=lambda item: item["center"], reverse=True)
        return [
            (item["left"], item["bottom"], item["right"], item["top"])
            for item in lines
        ]

    def add_highlight_overlays(self, quads: list[tuple[float, float, float, float]]) -> None:
        for left, bottom, right, top in quads:
            x = left * self.scale_factor
            y = (self.page_height - top) * self.scale_factor
            width = max(1.0, (right - left) * self.scale_factor)
            height = max(2.0, (top - bottom) * self.scale_factor)
            item = self.scene().addRect(
                x,
                y,
                width,
                height,
                QPen(Qt.PenStyle.NoPen),
                QBrush(QColor(255, 213, 88, 110)),
            )
            item.setZValue(1)
            self._highlight_items.append(item)

    def keyPressEvent(self, event) -> None:
        if event.matches(QKeySequence.StandardKey.Copy):
            self.copy_selection()
            return
        super().keyPressEvent(event)

    def copy_selection(self) -> None:
        if self._selected_text:
            QApplication.clipboard().setText(self._selected_text)

    def contextMenuEvent(self, event) -> None:
        from PySide6.QtWidgets import QMenu

        menu = QMenu(self)
        copy_action = menu.addAction("复制选区")
        copy_action.setEnabled(bool(self._selected_text))
        chosen = menu.exec(event.globalPos())
        if chosen is copy_action:
            self.copy_selection()


class PDFReaderDialog(QDialog):
    """Paginated PDF viewer with text selection and copy-safe highlights."""

    def __init__(self, path: Path, host, parent=None) -> None:
        super().__init__(parent or host)
        self.host = host
        self.pdf_path = path.expanduser().resolve()
        self.modified = False
        self.highlights: dict[int, list[tuple[float, float, float, float]]] = {}
        self._page = None
        self._text_page = None
        try:
            self.document = pdfium.PdfDocument(str(self.pdf_path))
        except Exception as exc:
            raise RuntimeError(f"无法打开 PDF：{exc}") from exc
        self.page_count = len(self.document)
        if not self.page_count:
            self.document.close()
            raise RuntimeError("PDF 文件中没有页面。")

        self.setWindowTitle(f"PDF 阅读 · {self.pdf_path.name}")
        self.resize(1080, 830)
        self.setMinimumSize(760, 560)
        self._build_ui()
        self._render_page(0)

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(9)

        toolbar = QHBoxLayout()
        self.page_number = QSpinBox()
        self.page_number.setRange(1, self.page_count)
        self.page_number.valueChanged.connect(lambda value: self._render_page(value - 1))
        self.page_label = QLabel(f"/ {self.page_count}")
        self.zoom = QComboBox()
        self.zoom.addItems(["75%", "90%", "100%", "115%", "130%"])
        self.zoom.setCurrentText("100%")
        self.zoom.currentTextChanged.connect(lambda _value: self._render_page(self.page_number.value() - 1))
        toolbar.addWidget(QLabel("页码"))
        toolbar.addWidget(self.page_number)
        toolbar.addWidget(self.page_label)
        toolbar.addSpacing(12)
        toolbar.addWidget(QLabel("缩放"))
        toolbar.addWidget(self.zoom)
        toolbar.addStretch(1)
        layout.addLayout(toolbar)

        actions = QHBoxLayout()
        self.copy_button = QPushButton("复制选区")
        self.copy_button.clicked.connect(self._copy_selection)
        self.paste_button = QPushButton("粘贴到笔记")
        self.paste_button.clicked.connect(self._paste_to_note)
        self.highlight_button = QPushButton("高亮选区")
        self.highlight_button.clicked.connect(self._add_highlight)
        self.save_button = QPushButton("保存高亮副本")
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save_highlight_copy)
        self.translate_button = QPushButton("AI 翻译选区")
        self.translate_button.clicked.connect(self._translate_selection)
        self.read_button = QPushButton("AI 精读 PDF")
        self.read_button.clicked.connect(self._read_with_ai)
        for button in (self.copy_button, self.paste_button, self.highlight_button, self.save_button,
                       self.translate_button, self.read_button):
            actions.addWidget(button)
        layout.addLayout(actions)

        self.selection_status = QLabel("拖动鼠标选择文字；Ctrl+C 复制选区。")
        self.selection_status.setObjectName("paneHint")
        layout.addWidget(self.selection_status)

        self.page_view = PDFPageView(self)
        self.page_view.selection_changed.connect(self._selection_changed)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.page_view)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        layout.addWidget(scroll, 1)

    def _render_page(self, page_index: int) -> None:
        page_index = max(0, min(page_index, self.page_count - 1))
        self.page_number.blockSignals(True)
        self.page_number.setValue(page_index + 1)
        self.page_number.blockSignals(False)
        self._release_page()
        self._page = self.document.get_page(page_index)
        self._text_page = self._page.get_textpage()
        zoom = int(self.zoom.currentText().rstrip("%")) / 100
        fit_width = max(420, self.width() - 70)
        scale = min(1.8, fit_width / max(1.0, self._page.get_width())) * zoom
        self.page_view.set_page(self._page, self._text_page, page_index, scale)
        for quad in self.highlights.get(page_index, []):
            self.page_view.add_highlight_overlays([quad])
        self.selection_status.setText("拖动鼠标选择文字；Ctrl+C 复制选区。")

    def _release_page(self) -> None:
        if self._text_page is not None:
            self._text_page.close()
            self._text_page = None
        if self._page is not None:
            self._page.close()
            self._page = None

    def _selection_changed(self, text: str) -> None:
        if text:
            display = text.replace("\n", " ").strip()
            if len(display) > 100:
                display = display[:100] + "…"
            self.selection_status.setText(f"已选中：{display}")
        else:
            self.selection_status.setText("拖动鼠标选择文字；Ctrl+C 复制选区。")

    def _copy_selection(self) -> None:
        if not self.page_view.selected_text:
            QMessageBox.information(self, "没有选区", "先在页面上拖动鼠标选中文字。")
            return
        self.page_view.copy_selection()
        self.selection_status.setText("已复制到剪贴板，可粘贴到笔记。")

    def _paste_to_note(self) -> None:
        text = self.page_view.selected_text
        if not text:
            QMessageBox.information(self, "没有选区", "先在页面上拖动鼠标选中文字。")
            return
        self.hide()
        self.host.paste_pdf_text(text)

    def _add_highlight(self) -> None:
        text = self.page_view.selected_text
        quads = self.page_view._selected_quads
        if not text or not quads:
            QMessageBox.information(self, "没有选区", "请选中 PDF 中可识别的文字后再添加高亮。")
            return
        page_index = self.page_view.page_index
        self.highlights.setdefault(page_index, []).extend(quads)
        self.page_view.add_highlight_overlays(quads)
        self.modified = True
        self.save_button.setEnabled(True)
        self.selection_status.setText("已添加高亮；原 PDF 未修改，保存后会生成高亮副本。")

    def save_highlight_copy(self) -> bool:
        if not self.highlights:
            QMessageBox.information(self, "暂无高亮", "先选中 PDF 文字并添加高亮。")
            return False
        default_path = self.pdf_path.with_name(f"{self.pdf_path.stem}_highlighted.pdf")
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "保存高亮副本",
            str(default_path),
            "PDF 文件 (*.pdf)",
        )
        if not filename:
            return False
        output = Path(filename).expanduser().resolve()
        if output == self.pdf_path:
            QMessageBox.warning(self, "不能覆盖原 PDF", "请选择其他文件名；原 PDF 会保持不变。")
            return False

        try:
            writer = PdfWriter(clone_from=str(self.pdf_path))
            for page_index, quads in self.highlights.items():
                for left, bottom, right, top in quads:
                    quad_points = ArrayObject(
                        [
                            FloatObject(left), FloatObject(top),
                            FloatObject(right), FloatObject(top),
                            FloatObject(left), FloatObject(bottom),
                            FloatObject(right), FloatObject(bottom),
                        ]
                    )
                    annotation = Highlight(
                        rect=(left, bottom, right, top),
                        quad_points=quad_points,
                        highlight_color="FFE082",
                    )
                    writer.add_annotation(page_index, annotation)
            with output.open("wb") as stream:
                writer.write(stream)
        except Exception as exc:
            QMessageBox.critical(self, "无法保存 PDF", str(exc))
            return False

        self.modified = False
        self.save_button.setEnabled(False)
        self.selection_status.setText(f"高亮副本已保存：{output}")
        return True

    def _translate_selection(self) -> None:
        text = self.page_view.selected_text
        if not text:
            QMessageBox.information(self, "没有选区", "先在页面上拖动鼠标选中文字。")
            return
        self.hide()
        self.host.translate_text_with_ai(text)

    def _read_with_ai(self) -> None:
        text = self.document_text()
        self.hide()
        self.host.read_text_with_ai(text, self.pdf_path.name)

    def document_text(self) -> str:
        page_texts: list[str] = []
        for page_index in range(self.page_count):
            page = self.document.get_page(page_index)
            text_page = page.get_textpage()
            try:
                text = text_page.get_text_range().strip()
            finally:
                text_page.close()
                page.close()
            if text:
                page_texts.append(f"[PDF 第 {page_index + 1} 页]\n{text}")
        return "\n\n".join(page_texts)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        if self._page is not None and hasattr(self, "zoom"):
            self._render_page(self.page_number.value() - 1)

    def closeEvent(self, event) -> None:
        if self.modified:
            choice = QMessageBox.question(
                self,
                "尚未保存高亮",
                "是否保存高亮副本后关闭？原始 PDF 不会被覆盖。",
                QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel,
                QMessageBox.StandardButton.Save,
            )
            if choice == QMessageBox.StandardButton.Save:
                if not self.save_highlight_copy():
                    event.ignore()
                    return
            elif choice == QMessageBox.StandardButton.Cancel:
                event.ignore()
                return
        self._release_page()
        self.document.close()
        event.accept()
