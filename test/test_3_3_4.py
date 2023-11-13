import pytest 
from src.E_3_3_4 import * 

def test_Conjunto1():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    resultado = Conjunto1(frutas1)
    assert resultado == {"manzana", "pera", "naranja", "plátano", "uva"}

def test_Conjunto2():
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
    resultado = Conjunto2(frutas2)
    assert resultado == {"manzana", "pera", "durazno", "sandía", "uva"}

def test_FrutasComunes():
    set_frutas_1 = {"manzana", "pera", "naranja", "plátano", "uva"}
    set_frutas_2 = {"manzana", "pera", "durazno", "sandía", "uva"}
    resultado = FrutasComunes(set_frutas_1, set_frutas_2)
    assert resultado == {"manzana", "pera", "uva"}

def test_unicosFrutas1():
    set_frutas_1 = {"manzana", "pera", "naranja", "plátano", "uva"}
    set_frutas_2 = {"manzana", "pera", "durazno", "sandía", "uva"}
    resultado = unicosFrutas1(set_frutas_1, set_frutas_2)
    assert resultado == {"naranja", "plátano"}

def test_unicosFrutas2():
    set_frutas_1 = {"manzana", "pera", "naranja", "plátano", "uva"}
    set_frutas_2 = {"manzana", "pera", "durazno", "sandía", "uva"}
    resultado = unicosFrutas2(set_frutas_1, set_frutas_2)
    assert resultado == {"durazno", "sandía"}

def test_mensajeSalida():
    set_frutas_1 = {"manzana", "pera", "naranja", "plátano", "uva"}
    set_frutas_2 = {"manzana", "pera", "durazno", "sandía", "uva"}
    frutas_comunes = {"manzana", "pera", "uva"}
    frutas_solo_1 = {"naranja", "plátano"}
    frutas_solo_2 = {"durazno", "sandía"}

    mensaje = mensajeSalida(set_frutas_1, set_frutas_2, frutas_comunes, frutas_solo_1, frutas_solo_2)

    assert "De los conjuntos" in mensaje
    assert str(set_frutas_1) in mensaje
    assert str(set_frutas_2) in mensaje
    assert "tienen las siguientes frutas iguales" in mensaje
    assert str(frutas_comunes) in mensaje
    assert "Frutas solo en conjunto 1:" in mensaje
    assert str(frutas_solo_1) in mensaje
    assert "Frutas solo en conjunto 2:" in mensaje
    assert str(frutas_solo_2) in mensaje