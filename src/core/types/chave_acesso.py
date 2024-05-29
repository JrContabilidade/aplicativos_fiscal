from datetime import date

from validate_docbr import CNPJ as ValidateCNPJ

from .insc_federal import Cnpj


class ChaveAcesso:
    def __init__(self, valor: str) -> None:
        """Representa uma chave de acesso

        Args:
        ---
            - valor (`str`): chave de acesso

        Exceptions
        ---
            - `ValueError`: Não é uma cahve de acesso válida
        """
        self._validar(valor)
        self._valor = valor

    def _validar(self, valor: str):

        valor_formatado = valor.strip()

        if len(valor_formatado) != 44:
            raise ValueError(
                f'A Chave {valor} de acesso não possui 44 caracteres.'
            )

        if valor.isnumeric(valor_formatado):
            raise ValueError(f'Chave {valor} possui valores não numericos.')

        mes = int(self._valor[2:4])

        if mes not in range(1, 13):
            raise ValueError(f'Chave {valor} possui mês invalido. {mes}')

        if ValidateCNPJ().validate(self._valor[6:20]):
            raise ValueError('Valor não corresponde um cnpj valido.')

    @property
    def cod_uf(self) -> int:
        """Código da UF do emitente do Documento Fiscal"""
        return int(self._valor[:2])

    @property
    def competencia(self) -> date:
        """Ano e Mês de emissão da NF-e"""
        mes = int(self._valor[2:4])
        ano = int(self._valor[4:6]) + 2000

        return date(ano, mes, 1)

    @property
    def cnpj(self) -> Cnpj:
        """CNPJ do emitente"""
        return Cnpj(self._valor[6:20])

    @property
    def modelo(self) -> int:
        """Modelo do Documento Fiscal"""
        return int(self._valor[20:22])

    @property
    def serie(self) -> int:
        """Série do Documento Fiscal"""
        return int(self._valor[22:25])

    @property
    def numero_nf(self) -> int:
        """Número do Documento Fiscal"""
        return int(self._valor[25:34])

    @property
    def tipo_emissao(self) -> int:
        """forma de emissão da NF-e"""
        return int(self._valor[34:35])

    @property
    def cod_numerico(self) -> int:
        """Código Numérico que compõe a Chave de Acesso"""
        return int(self._valor[35:43])

    @property
    def cod_verificador(self) -> int:
        """Dígito Verificador da Chave de Acesso"""
        return int(self._valor[43:44])

    def __str__(self) -> str:
        return self._chave

    def __repr__(self) -> str:
        return f"ChaveDeAceso('{self._valor}')"

    def __eq__(self, value: object) -> bool:
        chave_str = str(self)

        if isinstance(value, ChaveAcesso):
            return str(value) == chave_str

        if isinstance(value, str):
            return value == chave_str

        raise TypeError(
            f'Operção inválida para o tipo {type(value)}. Valor: {value}'
        )
