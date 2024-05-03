from dataclasses import dataclass
from pathlib import Path
from src.utils.path import get_exec_dir


@dataclass
class Settings:
    KEY = "AkeRmaeYtAja0SBZInrcSA0KWozYy6wC9okWT6FXNIU="
    CONFIGFILE = get_exec_dir() / "config.ini"


settings = Settings()
