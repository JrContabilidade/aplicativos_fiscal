from datetime import date
from decimal import Decimal

from pydantic import dataclasses

from src.external import get_questor_connection


@dataclasses.dataclass
class NotaQuestor:
    num_nf: int
    valor: Decimal
    chave_lcto: int
    chave_acesso: str | None
    insc_federal: str


def consultar_nf_questor(
    cod_empresa: int, cod_filial: int, data_inicio: date, data_final: date
):
    query = """
        SELECT L.NUMERONF, L.VALORCONTABIL, L.CHAVELCTOFISENT, L.CHAVENFEENT, P.INSCRFEDERAL 
        FROM LCTOFISENT L
        LEFT JOIN PESSOA P ON L.CODIGOPESSOA = P.CODIGOPESSOA 
        WHERE CODIGOEMPRESA = ?
        AND CODIGOESTAB = ?
        AND DATALCTOFIS BETWEEN ? AND ?
        """

    with get_questor_connection() as con:
        cursor = con.cursor()
        cursor.execute(
            query,
            (cod_empresa, cod_filial, data_inicio, data_final),
        )

        notas = cursor.fetchall()

    return [NotaQuestor(*nota) for nota in notas]
