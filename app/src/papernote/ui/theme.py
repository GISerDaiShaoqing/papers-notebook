from __future__ import annotations

import sys

from PySide6.QtGui import QFont


QSS = """
* { outline: none; }
QMainWindow, QDialog { background: #f3f6f7; }
QWidget { color: #273746; font-size: 13px; }
QFrame#topHeader { background: #ffffff; border-bottom: 1px solid #e2e9eb; }
QLabel#brandMark { color: #1e4859; font-size: 18px; font-weight: 700; }
QLabel#brandSubtitle { color: #778991; font-size: 11px; }
QWidget#sidebarPanel { background: #f8fafb; border-right: 1px solid #e2e9eb; }
QLabel#sectionEyebrow { color: #7c8d94; font-size: 10px; font-weight: 700; letter-spacing: 1px; }
QLabel#sidebarTitle { color: #1d3947; font-size: 17px; font-weight: 700; }
QLabel#noteCount { color: #84939a; font-size: 11px; }
QFrame#paneCard { background: #ffffff; border: 1px solid #e2e9eb; border-radius: 10px; }
QFrame#aiDrawer { background: #ffffff; border: 1px solid #d6e0e3; border-radius: 10px; }
QLabel#paneTitle { color: #294956; font-size: 13px; font-weight: 650; }
QLabel#paneHint { color: #87969c; font-size: 11px; }
QLineEdit#searchBox {
    background: #ffffff; border: 1px solid #d9e2e5; border-radius: 7px;
    padding: 8px 10px; selection-background-color: #2b7180; }
QLineEdit#searchBox:focus { border: 1px solid #4d9098; }
QTreeWidget#noteTree { background: transparent; border: none; padding: 3px; }
QTreeWidget#noteTree::item { min-height: 31px; padding: 3px 7px; border-radius: 6px; }
QTreeWidget#noteTree::item:hover { background: #edf3f4; }
QTreeWidget#noteTree::item:selected { background: #e2eff0; color: #1e5260; font-weight: 600; }
QPlainTextEdit#noteEditor {
    background: #ffffff; border: none; padding: 18px 20px; color: #293b43;
    selection-background-color: #dcecee; }
QTextBrowser#notePreview { background: #ffffff; border: none; }
QPushButton { background: #ffffff; border: 1px solid #d7e0e3; border-radius: 7px; padding: 7px 13px; color: #36505a; }
QPushButton:hover { background: #f1f6f6; border-color: #c4d5d8; }
QPushButton:pressed { background: #e5eff0; }
QPushButton#primaryButton { background: #2d6876; border: 1px solid #2d6876; color: #ffffff; font-weight: 600; padding: 8px 15px; }
QPushButton#primaryButton:hover { background: #245562; border-color: #245562; }
QPushButton#primaryButton:disabled { background: #a7bec2; border-color: #a7bec2; }
QStatusBar { background: #f3f6f7; border-top: 1px solid #e2e9eb; color: #71828a; }
QStatusBar::item { border: none; }
QMenuBar { background: #ffffff; border-bottom: 1px solid #e2e9eb; padding: 3px 7px; }
QMenuBar::item { padding: 5px 11px; border-radius: 5px; }
QMenuBar::item:selected { background: #edf3f4; }
QMenu { background: #ffffff; border: 1px solid #dbe3e5; padding: 5px; }
QMenu::item { padding: 6px 25px 6px 13px; border-radius: 4px; }
QMenu::item:selected { background: #e7f0f1; color: #245562; }
QScrollBar:vertical { background: transparent; width: 10px; margin: 2px; }
QScrollBar::handle:vertical { background: #cbd6d9; border-radius: 5px; min-height: 28px; }
QScrollBar::handle:vertical:hover { background: #aababe; }
QScrollBar:horizontal { background: transparent; height: 10px; margin: 2px; }
QScrollBar::handle:horizontal { background: #cbd6d9; border-radius: 5px; min-width: 28px; }
QScrollBar::add-line, QScrollBar::sub-line { height: 0; width: 0; }
QSplitter::handle { background: transparent; }
QSplitter::handle:horizontal { width: 6px; }
QSplitter::handle:hover { background: #dce7e9; border-radius: 3px; }
QToolTip { background: #243b45; color: #ffffff; border: none; padding: 5px 8px; }
"""


def apply_theme(app) -> None:
    app.setStyle("Fusion")
    if sys.platform == "darwin":
        app.setFont(QFont("PingFang SC", 13))
    elif sys.platform == "win32":
        app.setFont(QFont("Microsoft YaHei UI", 10))
    else:
        app.setFont(QFont("Noto Sans CJK SC", 10))
    app.setStyleSheet(QSS)
