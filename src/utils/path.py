from pathlib import Path
import sys
import os


def get_exec_dir():
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys.executable).parent
    else:
        return Path(os.getcwd())
