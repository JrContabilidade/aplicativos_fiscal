from decimal import Decimal
from tempfile import NamedTemporaryFile

from src.core.common import PydanticCsv
from src.core.impostos.comp_lanc_funrural.comp_lanc_funrural import NumNFValorModel


def test_pydantic_csv():
    with NamedTemporaryFile("w+") as temp_file:
        temp_file.write(
            """nota;valor
117;52.000,00
118;5.000,00
119;309,69
120;856,11
104122;75.309,45
104123;71.886,67
122;55.000,00
123;11;11"""
        )
        temp_file.flush()

        csv = PydanticCsv(NumNFValorModel)
        registros = csv.load_csv(temp_file.name)

        assert len(registros) == 9

        assert registros[1].registro.num_nf == 117
        assert registros[1].registro.valor == Decimal("52000")
