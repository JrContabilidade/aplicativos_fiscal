from PySide6.QtWidgets import QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, Qt


class Documentacao(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1366, 768)
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.setWindowTitle("Documentação")
        self.web_view = QWebEngineView(self)
        self.setCentralWidget(self.web_view)

    def set_url(self, url: str):
        self.web_view.load(QUrl(url))
