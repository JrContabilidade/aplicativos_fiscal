from __future__ import annotations

import re

from validate_docbr import CNPJ as ValidateCNPJ

from .protocols import InscFederal


class Cnpj:
    def __init__(self, valor: str) -> None:
        """Representa um CNPJ

        Args:
        ---
            - valor (`str`): Valor CNPJ

        Raises
        ---
            - `ValueError`: Erro ao validar CNPJ
        """

        self._validar(valor)
        self._valor = self._formatar(valor)

    def _validar(self, valor: str):

        validate = ValidateCNPJ()
        if not validate.validate(valor):
            raise ValueError('Valor não corresponde um cnpj valido.')

    def _formatar(self, valor: str):
        valor_formatado = re.sub('[^0-9]', '', valor)
        valor_formatado = valor_formatado.zfill(14)

        return valor_formatado

    @property
    def com_pontuacao(self) -> str:
        validate = ValidateCNPJ()
        return validate.mask(self._valor)

    @property
    def sem_pontuacao(self) -> str:
        return self._valor

    @property
    def raiz(self) -> str:
        return self._valor[:8]

    def __repr__(self) -> str:
        return f"Cnpj('{self._valor}')"

    def __str__(self) -> str:
        return self._valor

    def __eq__(self, __value) -> bool:
        if isinstance(__value, InscFederal):
            return __value.sem_pontuacao == self.sem_pontuacao

        if isinstance(__value, str):
            return Cnpj(__value).com_pontuacao == self.com_pontuacao

        raise TypeError(
            f'Operção inválida para o tipo {type(__value)}. Valor: {__value}'
        )
