from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtCore import Qt
from .main_ui import Ui_MainWindow
from src.desktop.screens.configuracoes import QuestorDB
from src.desktop.screens.impostos import CompLancFunrural
from src.desktop.screens.ajuda import Documentacao


class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.open_windows: list[QWidget] = []

        self.ui.act_banco_questor.triggered.connect(
            lambda: self.add_sub_window(QuestorDB(self))
        )
        self.ui.act_comp_lanc_funrural.triggered.connect(
            lambda: self.add_sub_window(CompLancFunrural(self))
        )

        self.ui.act_documentacao.triggered.connect(self.show_documentacao)

    def add_sub_window(self, widget: QWidget):

        for window in self.open_windows:
            if isinstance(widget, type(window)):
                return

        self.open_windows.append(widget)
        subwindow = self.ui.mdi_area.addSubWindow(widget)
        subwindow.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        subwindow.destroyed.connect(lambda: self.open_windows.remove(widget))

        subwindow.show()

    def show_documentacao(self):
        doc = Documentacao(self)
        doc.set_url("http://127.0.0.1:8000/")
        doc.show()
