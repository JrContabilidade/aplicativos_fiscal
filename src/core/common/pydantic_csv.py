from __future__ import annotations
import csv
from typing import TypeVar

from loguru import logger
from pydantic import ValidationError, dataclasses

T = TypeVar("T")


@dataclasses.dataclass
class _RegistroError:
    columns: list[int]
    msgs: list[str]

    @property
    def detail(self) -> str:
        return ", ".join(
            [f"coluna {col}: {msg}" for col, msg in zip(self.columns, self.msgs)]
        )


@dataclasses.dataclass
class _Registro[T]:
    num_linha: int
    linha: str
    registro: T | None = None
    error: _RegistroError | None = None


class PydanticCsv[T]:

    def __init__(
        self, pydantic_model: type[T], delimiter: str = ";", encoding="latin-1"
    ):
        self._model = pydantic_model
        self._delimiter = delimiter
        self._encoding = encoding

    def _make_registro_error(self, err: ValidationError):
        invalidas = [int(error["loc"][0]) for error in err.errors()]
        msgs = [error["msg"] for error in err.errors()]
        return _RegistroError(invalidas, msgs)

    def load_csv(self, file_path: str) -> list[_Registro[T]]:

        registros = []

        with open(file_path, "r", encoding=self._encoding) as file:
            logger.debug("Lendo arquivo {}", file_path)
            reader = csv.reader(file, delimiter=self._delimiter)
            fields = self._model.__annotations__.keys()

            for line in reader:
                num_linha = reader.line_num
                linha = self._delimiter.join(line)
                values = line[: len(fields)]

                logger.debug("Lendo {}: {}", num_linha, linha)

                try:
                    r = self._model(*values)
                    registro = _Registro(num_linha=num_linha, linha=linha, registro=r)
                    registros.append(registro)
                except ValidationError as err:
                    error = self._make_registro_error(err)
                    logger.warning("Erros: {}", error.detail)
                    registro = _Registro(num_linha=num_linha, linha=linha, error=error)
                    registros.append(registro)

        return registros

    @property
    def delimiter(self):
        return self._delimiter
