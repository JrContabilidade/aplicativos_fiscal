import os
import sys
from pathlib import Path

from decouple import config

if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    ROOT_PATH = Path(sys.executable).parent
else:
    ROOT_PATH = Path(os.getcwd())

SECRET_KEY = "AkeRmaeYtAja0SBZInrcSA0KWozYy6wC9okWT6FXNIU="

QUESTOR_DB = config("QUESTOR_DB", default="")
QUESTOR_DB_USER = config("QUESTOR_DB_USER", default="")
QUESTOR_DB_PASSWORD = config("QUESTOR_DB_PASSWORD", default="")
QUESTOR_DB_HOST = config("QUESTOR_DB_HOST", default="")
QUESTOR_DB_PORT = config("QUESTOR_DB_PORT", default=3050, cast=int)

DOC_URL = config("DOC_URL", default="")

CONFIG_FILE = ROOT_PATH / "settings.ini"
