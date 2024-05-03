from __future__ import annotations

from PySide6.QtWidgets import QMessageBox, QWidget

from .questor_db_ui import Ui_QuestorDB
from src.settings.questor_db import db_settings


class QuestorDB(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.ui = Ui_QuestorDB()
        self.ui.setupUi(self)

        self.ui.btn_salvar.clicked.connect(self.salvar)
        self._load_config_file()

    def _validate(self):

        erros: list[str] = []

        banco = self.ui.txt_banco.text()
        usuario = self.ui.txt_usuario.text()
        senha = self.ui.txt_senha.text()
        host = self.ui.txt_host.text()
        porta = self.ui.txt_porta.text()

        if not banco:
            erros.append("Campo banco é obrigatorio")

        if not usuario:
            erros.append("Campo Usuário é obrigatorio")

        if not senha:
            erros.append("Campo Senha é obrigatorio")

        if not host:
            erros.append("Campo Host é obrigatorio")

        if not porta:
            erros.append("Campo Porta é obrigatorio")

        return erros

    def _load_config_file(self):
        try:
            self.ui.txt_banco.setText(db_settings.banco)
            self.ui.txt_usuario.setText(db_settings.usuario)
            self.ui.txt_senha.setText(db_settings.senha)
            self.ui.txt_host.setText(db_settings.host)
            self.ui.txt_porta.setValue(int(db_settings.porta))
        except FileNotFoundError:
            pass

    def salvar(self):
        erros = self._validate()

        if erros:
            message = "\n".join(erros)
            QMessageBox.warning(self, "Erros de validação.", message)
            return

        db_settings.banco = self.ui.txt_banco.text()
        db_settings.usuario = self.ui.txt_usuario.text()
        db_settings.senha = self.ui.txt_senha.text()
        db_settings.host = self.ui.txt_host.text()
        db_settings.porta = self.ui.txt_porta.text()

        db_settings.save()

        QMessageBox.information(self, "Sucesso", "Salvo com sucesso...")

        self.parent().close()
