from __future__ import annotations

import os
import sys
from pathlib import Path

from decouple import config

from src.utils.encrypt_decrypt import decrypt


def _get_path_root():
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return Path(sys.executable).parent

    return Path(os.getcwd())


class Setting:
    ROOT_PATH = _get_path_root()

    SECRET_KEY = 'AkeRmaeYtAja0SBZInrcSA0KWozYy6wC9okWT6FXNIU='

    QUESTOR_DB = config('QUESTOR_DB', default='')
    QUESTOR_DB_USER = config('QUESTOR_DB_USER', default='')
    QUESTOR_DB_PASSWORD = decrypt(
        SECRET_KEY, config('QUESTOR_DB_PASSWORD', default='')
    )
    QUESTOR_DB_HOST = config('QUESTOR_DB_HOST', default='')
    QUESTOR_DB_PORT = config('QUESTOR_DB_PORT', default=3050, cast=int)

    DOC_URL = config('DOC_URL', default='')

    CONFIG_FILE = ROOT_PATH / 'settings.ini'


settings = Setting()
