import re


class OutraInscFederal:
    def __init__(self, valor: str) -> None:
        self._valor = valor

    def _formatar(self, valor: str):
        valor_formatado = re.sub('[^0-9]', '', valor)

        return valor_formatado

    @property
    def com_pontuacao(self) -> str:
        return self._valor

    @property
    def sem_pontuacao(self) -> str:
        return self._formatar(self._valor)
