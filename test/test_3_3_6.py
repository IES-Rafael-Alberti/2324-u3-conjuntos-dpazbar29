import pytest 
from src.E_3_3_6 import * 

def test_consonantes():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    abecedario = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"}
    resultado = consonantes(vocales, abecedario)
    assert resultado == {"b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"}

def test_letrasComunes():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    cons = {"b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"}
    resultado = letrasComunes(vocales, cons)
    assert resultado == set()

def test_mensajeSalida():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    cons = {"b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"}
    letras_comunes = letrasComunes(vocales, cons)
    
    mensaje = mensajeSalida(cons, letras_comunes)

    assert "Consonantes:" in mensaje
    assert str(cons) in mensaje
    assert "Letras comunes:" in mensaje
    assert str(letras_comunes) in mensaje
