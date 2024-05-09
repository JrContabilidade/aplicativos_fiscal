import sys


def is_bundle():
    return getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS")


def is_debug():
    pass
