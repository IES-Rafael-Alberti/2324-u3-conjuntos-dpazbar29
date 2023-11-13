import pytest 
from src.E_3_3_5 import * 

def test_pares():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    resultado = pares(numeros)
    assert resultado == {0,2, 4, 6, 8, 10}

def test_multiplosTres():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    resultado = multiplosTres(numeros)
    assert resultado == {3, 6, 9}

def test_interseccionParesMultiplosTres():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    par = pares(numeros)
    multiplos_de_tres = multiplosTres(numeros)
    resultado = interseccionParesMultiplosTres(par, multiplos_de_tres)
    assert resultado == {6}

def test_mensajeSalida():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    par = pares(numeros)
    multiplos_de_tres = multiplosTres(numeros)
    interseccion = interseccionParesMultiplosTres(par, multiplos_de_tres)
    
    mensaje = mensajeSalida(par, multiplos_de_tres, interseccion)

    assert "Lo numeros pares son:" in mensaje
    assert str(par) in mensaje
    assert "Numeros impares:" in mensaje
    assert str(multiplos_de_tres) in mensaje
    assert "Numeros pares y múltiplos de 3 coincidentes:" in mensaje
    assert str(interseccion) in mensaje