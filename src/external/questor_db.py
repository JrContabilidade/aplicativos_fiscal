from firebirdsql import connect
from src.settings import settings


def get_questor_connection():

    return connect(
        database=settings.QUESTOR_DB,
        user=settings.QUESTOR_DB_USER,
        password=settings.QUESTOR_DB_PASSWORD,
        host=settings.QUESTOR_DB_HOST,
        port=settings.QUESTOR_DB_PORT,
        charset="ISO8859_1",
    )
