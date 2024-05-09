from decimal import Decimal, InvalidOperation
from datetime import date

from loguru import logger
from pydantic import dataclasses, field_validator

from src.core.common import PydanticCsv

from .consulta_nfs_questor import consultar_nf_questor, NotaQuestor


@dataclasses.dataclass
class NumNFValorModel:
    num_nf: int
    valor: Decimal

    @field_validator("valor", mode="before")
    @classmethod
    def convert_para_decimal(cls, v: str) -> Decimal:
        try:
            return Decimal(v.translate(str.maketrans(",", ".", ".R$ ")))
        except InvalidOperation:
            raise ValueError(f"{v} não é um valor válido.")


class ComparativoLancamentoFunrural:

    def __init__(
        self,
        arq_funrural: str,
        cod_empresa: int,
        cod_filial: int,
        data_inicio: date,
        data_final: date,
    ) -> None:
        self._arq_funrural = arq_funrural
        self._cod_empresa = cod_empresa
        self._cod_filial = cod_filial
        self._data_inicio = data_inicio
        self._data_final = data_final

        self._csv_result: str = ""
        self._chaves_lctos: list[int] = []

    def _buscar_nota_questor(
        self, notas_questor: list[NotaQuestor], nota_csv: NumNFValorModel
    ):
        for nota_questor in notas_questor:
            v_questor = (nota_csv.registro.num_nf, nota_csv.registro.valor)
            v_csv = (nota_questor.num_nf, nota_questor.valor)

            if v_questor == v_csv:
                return nota_questor

    def processar(self):
        csv = PydanticCsv(NumNFValorModel)
        notas_csv = csv.load_csv(self._arq_funrural)

        notas_questor = consultar_nf_questor(
            self._cod_empresa, self._cod_filial, self._data_inicio, self._data_final
        )

        for nota_csv in notas_csv:
            if nota_csv.error:
                self._csv_result += (
                    nota_csv.linha + f";colunas {nota_csv.error.columns} inválidas\n"
                )

            else:
                nota_encontrada = self._buscar_nota_questor(notas_questor, nota_csv)

                if nota_encontrada:
                    chave_lcto = nota_encontrada.chave_lcto
                    self._csv_result += (
                        nota_csv.linha + f";encontrada - chave: {chave_lcto}\n"
                    )
                    self._chaves_lctos.append(nota_encontrada.chave_lcto)

                else:
                    self._csv_result += nota_csv.linha + ";não encontrada\n"

        logger.success(
            "Empresa: {} | Filial: {} | Inicio: {} | Final: {} | Encontradas: {}",
            self._cod_empresa,
            self._cod_filial,
            self._data_inicio,
            self._data_final,
            len(self._chaves_lctos),
        )

    @property
    def csv_result(self):
        return self._csv_result

    @property
    def chaves_lctos(self):
        return self._chaves_lctos
