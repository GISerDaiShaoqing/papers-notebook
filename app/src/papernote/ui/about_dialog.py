from __future__ import annotations

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QDialog, QFrame, QHBoxLayout, QLabel, QPushButton, QVBoxLayout

from .. import (
    APP_AUTHOR,
    APP_AUTHOR_URL,
    APP_LICENSE,
    APP_NAME,
    APP_REPOSITORY_URL,
    APP_TAGLINE,
    __version__,
)


class AboutDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("关于")
        self.setMinimumWidth(500)
        self.setModal(True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(26, 25, 26, 20)
        layout.setSpacing(15)

        title_row = QHBoxLayout()
        title = QLabel(APP_NAME)
        title.setStyleSheet("font-size: 20px; font-weight: 700; color: #263d48;")
        version = QLabel(f"v{__version__}")
        version.setStyleSheet("font-size: 13px; color: #4b78ba; padding-top: 4px;")
        title_row.addWidget(title)
        title_row.addWidget(version, alignment=Qt.AlignmentFlag.AlignBottom)
        title_row.addStretch(1)
        layout.addLayout(title_row)

        tagline = QLabel(APP_TAGLINE)
        tagline.setStyleSheet("font-size: 13px; color: #7b8995;")
        layout.addWidget(tagline)

        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.setStyleSheet("color: #e7ebef;")
        layout.addWidget(divider)

        author = QLabel(f"作者：{APP_AUTHOR}")
        author.setStyleSheet("font-size: 13px; color: #374854;")
        layout.addWidget(author)

        links = QLabel(
            f'<a href="{APP_AUTHOR_URL}">GitHub 主页</a>'
            " &nbsp;·&nbsp; "
            f'<a href="{APP_REPOSITORY_URL}">项目仓库</a>'
        )
        links.setTextFormat(Qt.TextFormat.RichText)
        links.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        links.setOpenExternalLinks(False)
        links.linkActivated.connect(lambda url: QDesktopServices.openUrl(QUrl(url)))
        links.setStyleSheet("font-size: 13px; color: #4b78ba;")
        layout.addWidget(links)

        license_text = QLabel(APP_LICENSE)
        license_text.setStyleSheet("font-size: 12px; color: #87939f;")
        layout.addWidget(license_text)

        footer = QHBoxLayout()
        footer.addStretch(1)
        close_button = QPushButton("关闭")
        close_button.clicked.connect(self.accept)
        close_button.setDefault(True)
        footer.addWidget(close_button)
        layout.addLayout(footer)
