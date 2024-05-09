from src.desktop import show_screen
from src.infraestructure import loading, make_logs


def exec_app():
    loading()
    make_logs()
    show_screen()
