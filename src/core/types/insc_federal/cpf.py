# pylint: disable=C0114
import re

from validate_docbr import CPF as ValidateCPF


class Cpf:
    def __init__(self, valor: str) -> None:
        """Representa um CPF

        Args:
        ---
            - valor (`str`): Valor CPF

        Raises
        ---
            - `ValueError`: Erro ao validar CPF
        """

        self._validar(valor)
        self._valor = self._formatar(valor)

    def _validar(self, valor: str):
        validate = ValidateCPF()
        if not validate.validate(valor):
            raise ValueError('Valor não corresponde um cpf valido.')

    def _formatar(self, valor: str):
        valor_formatado = re.sub('[^0-9]', '', valor)
        valor_formatado = valor_formatado.zfill(11)

        return valor_formatado

    @property
    def com_pontuacao(self) -> str:
        validate = ValidateCPF()
        return validate.mask(self._valor)

    @property
    def sem_pontuacao(self) -> str:
        return self._valor

    def __repr__(self) -> str:
        return f"Cpf('{self.sem_pontuacao}')"

    def __str__(self) -> str:
        return self.sem_pontuacao

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Cpf):
            return False

        return __value.sem_pontuacao == self.sem_pontuacao
