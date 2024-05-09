from pathlib import Path
import sys
import os

from .checks import is_bundle


def get_exec_dir():
    if is_bundle():
        return Path(sys.executable).parent
    else:
        return Path(os.getcwd())
