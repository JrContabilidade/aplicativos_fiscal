from firebirdsql import connect
from src.settings.questor_db import db_settings


def get_questor_connection():

    return connect(
        database=db_settings.banco,
        user=db_settings.usuario,
        password=db_settings.senha,
        host=db_settings.host,
        port=db_settings.porta,
        charset="ISO8859_1",
    )
