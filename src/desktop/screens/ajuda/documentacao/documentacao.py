from PySide6.QtCore import Qt, QUrl
from PySide6.QtWidgets import QMainWindow


class Documentacao(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1366, 768)
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.setWindowTitle("Documentação")
