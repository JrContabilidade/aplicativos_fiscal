from src.core.impostos.comp_lanc_funrural import ComparativoLancamentoFunrural
from tempfile import NamedTemporaryFile
from datetime import date

# from unittest.mock import patch, Mock


# @patch(
#     "src.core.impostos.comp_lanc_funrural.consulta_nfs.consultar_nf_questor",
#     Mock(return_value=[]),
# )
def test_comp_lanc_funrural_por_nf_valor():

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

        comp = ComparativoLancamentoFunrural(
            temp_file.name, 1494, 1, date(2024, 3, 1), date(2024, 3, 31)
        )

        comp.processar()
