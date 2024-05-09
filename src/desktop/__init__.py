import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from .screens.main import Main


def show_screen():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    window.setWindowState(Qt.WindowState.WindowActive)
    app.exec()
