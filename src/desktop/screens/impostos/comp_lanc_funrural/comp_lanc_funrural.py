import shutil
from datetime import date

import pyperclip
from PySide6.QtCore import QDate, QObject, QRunnable, QThreadPool, Signal
from PySide6.QtWidgets import QFileDialog, QWidget

from src.core.impostos.comp_lanc_funrural import (
    ComparativoLancamentoFunrural,
    gerar_arquivo_modelo,
)

from .comp_lanc_funrural_ui import Ui_CompLancFunrural


class Signals(QObject):
    started = Signal()
    finished = Signal()
    success = Signal(list, str)
    error = Signal()


class Worker(QRunnable):

    def __init__(
        self,
        arq_funrural: str,
        cod_empresa: int,
        cod_filial: int,
        data_inicio: date,
        data_final: date,
    ) -> None:
        super().__init__()
        self.signals = Signals()

        self._arq_funrural = arq_funrural
        self._cod_empresa = cod_empresa
        self._cod_filial = cod_filial
        self._data_inicio = data_inicio
        self._data_final = data_final

    def run(self) -> None:
        self.signals.started.emit()

        comparativo = ComparativoLancamentoFunrural(
            self._arq_funrural,
            self._cod_empresa,
            self._cod_filial,
            self._data_inicio,
            self._data_final,
        )

        comparativo.processar()
        self.signals.finished.emit()
        self.signals.success.emit(comparativo.chaves_lctos, comparativo.csv_result)


class CompLancFunrural(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.ui = Ui_CompLancFunrural()
        self.ui.setupUi(self)

        self.threadpool = QThreadPool(self)

        today = date.today()

        self.ui.txt_data_inicio.setDate(QDate(today.year, today.month, 1))
        self.ui.txt_data_final.setDate(QDate().currentDate())

        self.ui.txt_empresa.clear()
        self.ui.txt_filial.clear()

        self.ui.btn_arq_funrural.pressed.connect(self.selecionar_arquivo)
        self.ui.btn_limpar.pressed.connect(self.limpar)
        self.ui.btn_processar.pressed.connect(self.processar)
        self.ui.btn_copiar.pressed.connect(self.copiar_chaves_lcto)
        self.ui.btn_baixar_modelo.pressed.connect(self.baixar_arquivo_modelo)

    def _process_started(self):
        self.ui.btn_arq_funrural.setDisabled(True)
        self.ui.btn_copiar.setDisabled(True)
        self.ui.btn_baixar_modelo.setDisabled(True)
        self.ui.btn_limpar.setDisabled(True)
        self.ui.btn_processar.setDisabled(True)

        self.ui.txt_arq_funrural.setReadOnly(True)
        self.ui.txt_empresa.setReadOnly(True)
        self.ui.txt_filial.setReadOnly(True)
        self.ui.txt_data_inicio.setReadOnly(True)
        self.ui.txt_data_final.setReadOnly(True)
        self.ui.txt_chaves_lcto.setReadOnly(True)

    def _process_finished(self):
        self.ui.btn_arq_funrural.setDisabled(False)
        self.ui.btn_copiar.setDisabled(False)
        self.ui.btn_baixar_modelo.setDisabled(False)
        self.ui.btn_limpar.setDisabled(False)
        self.ui.btn_processar.setDisabled(False)

        self.ui.txt_arq_funrural.setReadOnly(False)
        self.ui.txt_empresa.setReadOnly(False)
        self.ui.txt_filial.setReadOnly(False)
        self.ui.txt_data_inicio.setReadOnly(False)
        self.ui.txt_data_final.setReadOnly(False)
        self.ui.txt_chaves_lcto.setReadOnly(False)

    def _process_sucess(self, chaves_lcto: list[int], csv_result: str):
        chaves = ";".join([str(chave) for chave in chaves_lcto])
        self.ui.txt_chaves_lcto.setPlainText(chaves)

        file = self.ui.txt_arq_funrural.text()
        bkp_file = file.replace(".csv", "") + "_bkp.csv"

        shutil.copyfile(file, bkp_file)

        with open(file, "w", encoding="latin-1") as file_instance:
            file_instance.write(csv_result)

    def copiar_chaves_lcto(self):
        text = self.ui.txt_chaves_lcto.toPlainText()
        pyperclip.copy(text)

    def selecionar_arquivo(self):

        filename, _ = QFileDialog.getOpenFileName(
            self, "Selecionar Arquivo CSV", filter="Arquivo CSV (*.csv)"
        )

        if filename:
            self.ui.txt_arq_funrural.setText(filename)

    def baixar_arquivo_modelo(self):
        save_file, _ = QFileDialog.getSaveFileName(
            self, "Salvar como...", filter=("Arquivo CSV (*.csv)")
        )

        if save_file:
            gerar_arquivo_modelo(save_file)

    def limpar(self):
        self.ui.txt_arq_funrural.clear()
        self.ui.txt_empresa.clear()
        self.ui.txt_filial.clear()
        self.ui.txt_chaves_lcto.clear()

    def processar(self):

        arq_funrural = self.ui.txt_arq_funrural.text()
        cod_empresa = self.ui.txt_empresa.value()
        cod_filial = self.ui.txt_filial.value()
        data_inicio = self.ui.txt_data_inicio.date().toPython()
        data_final = self.ui.txt_data_final.date().toPython()

        worker = Worker(arq_funrural, cod_empresa, cod_filial, data_inicio, data_final)

        worker.signals.started.connect(self._process_started)
        worker.signals.success.connect(self._process_sucess)
        worker.signals.finished.connect(self._process_finished)

        self.threadpool.start(worker)
