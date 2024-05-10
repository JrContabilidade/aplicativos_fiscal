from firebirdsql import connect
from src.settings import (
    QUESTOR_DB,
    QUESTOR_DB_USER,
    QUESTOR_DB_PASSWORD,
    QUESTOR_DB_HOST,
    QUESTOR_DB_PORT,
)


def get_questor_connection():

    return connect(
        database=QUESTOR_DB,
        user=QUESTOR_DB_USER,
        password=QUESTOR_DB_PASSWORD,
        host=QUESTOR_DB_HOST,
        port=QUESTOR_DB_PORT,
        charset="ISO8859_1",
    )
