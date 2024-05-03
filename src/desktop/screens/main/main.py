from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtCore import Qt
from .main_ui import Ui_MainWindow
from src.desktop.screens.configuracoes import QuestorDB


class Main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.open_windows: list[QWidget] = []

        self.ui.act_banco_questor.triggered.connect(
            lambda: self.add_sub_window(QuestorDB(self))
        )

    def add_sub_window(self, widget: QWidget):

        for window in self.open_windows:
            if isinstance(widget, type(window)):
                return

        self.open_windows.append(widget)
        subwindow = self.ui.mdi_area.addSubWindow(widget)
        subwindow.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        subwindow.destroyed.connect(lambda: self.open_windows.remove(widget))

        subwindow.show()
