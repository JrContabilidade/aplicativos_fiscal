from __future__ import annotations

import os
import sys
from configparser import ConfigParser

from PySide6.QtWidgets import QMessageBox, QWidget

from src.settings import settings
from src.utils.encrypt_decrypt import encrypt

from .questor_db_ui import Ui_QuestorDB


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

        senha = settings.QUESTOR_DB_PASSWORD

        self.ui.txt_banco.setText(settings.QUESTOR_DB)
        self.ui.txt_usuario.setText(settings.QUESTOR_DB_HOST)
        self.ui.txt_senha.setText(senha)
        self.ui.txt_host.setText(settings.QUESTOR_DB_USER)
        self.ui.txt_porta.setValue(int(settings.QUESTOR_DB_PORT))

    def salvar(self):

        erros = self._validate()

        if erros:
            message = "\n".join(erros)
            QMessageBox.warning(self, "Erros de validação.", message)
            return

        banco = self.ui.txt_banco.text()
        usuario = self.ui.txt_usuario.text()
        senha = self.ui.txt_senha.text()
        host = self.ui.txt_host.text()
        porta = self.ui.txt_porta.text()

        senha = encrypt(settings.SECRET_KEY, senha)

        config = ConfigParser()

        with open(settings.CONFIG_FILE, "r") as file:
            config = ConfigParser()
            config.read_file(file)
            config.set("settings", "QUESTOR_DB", banco)
            config.set("settings", "QUESTOR_DB_USER", usuario)
            config.set("settings", "QUESTOR_DB_PASSWORD", senha)
            config.set("settings", "QUESTOR_DB_HOST", host)
            config.set("settings", "QUESTOR_DB_PORT", porta)

        with open(settings.CONFIG_FILE, "w") as file:
            config.write(file)

        QMessageBox.information(
            self,
            "Sucesso",
            "O sistema será finalizado e as configurações serão recarregadas na proxima inicialização...",
        )

        sys.exit()
