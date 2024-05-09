from typing import Protocol, runtime_checkable


@runtime_checkable
class InscFederal(Protocol):
    @property
    def com_pontuacao(self) -> str: ...

    @property
    def sem_pontuacao(self) -> str: ...
