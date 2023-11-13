import pytest 
from src.E_3_3_2 import * 

def test_nombresTotal():
    nombres_primaria = {"Juan", "María", "Carlos"}
    nombres_secundaria = {"Ana", "Carlos", "Pedro"}

    resultado = nombresTotal(nombres_primaria, nombres_secundaria)

    # Verifica que todos los elementos esperados estén presentes en el conjunto resultado
    assert "Juan" in resultado
    assert "María" in resultado
    assert "Carlos" in resultado
    assert "Ana" in resultado
    assert "Pedro" in resultado

def test_PrimariaNoRepetidoSecudanria():
    nombres_primaria = {"Juan", "María", "Carlos"}
    nombres_secundaria = {"Ana", "Carlos", "Pedro"}

    resultado = PrimariaNoRepetidoSecudanria(nombres_primaria, nombres_secundaria)

    # Verifica que el conjunto resultado contenga los nombres de primaria no repetidos en secundaria
    assert "Juan" in resultado
    assert "María" in resultado

    # Verifica que el conjunto resultado no contenga nombres repetidos en ambos grados
    assert not ("Carlos" in resultado)

def test_PrimariaEnSecundaria():
    nombres_primaria = {"Juan", "María", "Carlos"}
    nombres_secundaria = {"Ana", "Carlos", "Pedro", "Juan", "María"}

    resultado = PrimariaEnSecundaria(nombres_primaria, nombres_secundaria)

    # Verifica que la salida sea la esperada
    assert resultado == "Los nombres de primaria están incluidos en secundaria"
    

def test_mensajeSalida():
    nombres_sin_repetir = "Juan,María,Carlos,Ana,Pedro"
    nombres_repetidos = "Carlos"
    nombres_primaria_secundaria = "Juan,María"
    nombres_primaria_incluidos_secundaria = "Los nombres de primaria están incluidos en secundaria"

    mensaje = mensajeSalida(nombres_sin_repetir, nombres_repetidos, nombres_primaria_secundaria, nombres_primaria_incluidos_secundaria)

    # Verifica que el mensaje tenga el formato esperado
    assert "Nombres totales: Juan,María,Carlos,Ana,Pedro" in mensaje
    assert "Nombres repetidos: Carlos" in mensaje
    assert "Nombres primaria no repetidos en secundaria: Juan,María" in mensaje
    assert "Nombres primaria incluidos en secundaria: Los nombres de primaria están incluidos en secundaria" in mensaje