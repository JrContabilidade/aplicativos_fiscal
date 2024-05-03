import sys
from PySide6.QtWidgets import QApplication

from .screens.main import Main


def show_screen():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec()
