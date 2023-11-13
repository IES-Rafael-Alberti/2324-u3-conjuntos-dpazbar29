import pytest 
from src.E_3_3_1 import * 

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ([("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),("Jorge Russo", 7, 699, "Mirasol 218"),("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),("Jorge Russo", 15, 958, "Mirasol 218")],['Calle Las Flores 355', 'La Mancha 761', 'Mirasol 218'])
    ]
)

def test_obtenerDomiciliosFacturas(input_x,expected):
    assert obtenerDomiciliosFacturas(input_x) == expected