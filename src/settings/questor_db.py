from __future__ import annotations

from configparser import ConfigParser
from dataclasses import dataclass

from cryptography.fernet import Fernet

from src.settings.globals import settings


@dataclass
class DBSettings:
    banco: str
    usuario: str
    senha: str
    host: str
    porta: str

    @staticmethod
    def from_file() -> DBSettings:

        if not settings.CONFIGFILE.exists():
            db_settings = DBSettings("", "", "", "", "0")
            db_settings.save()
            return db_settings

        fernet = Fernet(settings.KEY)

        with open(settings.CONFIGFILE, "r") as file:
            config = ConfigParser()
            config.read_file(file)

        senha_decript = fernet.decrypt(config["banco"]["senha"].encode()).decode()

        return DBSettings(
            config["banco"]["banco"],
            config["banco"]["usuario"],
            senha_decript,
            config["banco"]["host"],
            config["banco"]["porta"],
        )

    def save(self):

        fernet = Fernet(settings.KEY)

        senha_cript = fernet.encrypt(self.senha.encode()).decode()

        with open(settings.CONFIGFILE, "w") as file:
            config = ConfigParser()
            config["banco"] = {
                "banco": self.banco,
                "usuario": self.usuario,
                "senha": senha_cript,
                "host": self.host,
                "porta": self.porta,
            }
            config.write(file)


db_settings = DBSettings.from_file()
