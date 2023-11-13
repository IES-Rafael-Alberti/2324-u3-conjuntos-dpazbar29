#3.3.6

def consonantes(vocales,abecedario):
    resultado = abecedario - vocales
    return set(resultado)

def letrasComunes(vocales,cons):
    resultado = vocales & cons
    return set(resultado)

def mensajeSalida(cons,letras_comunes):
    mensaje = "Consonantes: " + str(cons) + "\nLetras comunes: " + str(letras_comunes)
    return mensaje


if __name__ == "__main__":

    #entrada
    vocales = {'a', 'e', 'i', 'o', 'u'}
    abecesario = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"}

    #proceso
    cons = consonantes(vocales,abecesario)
    letras_comunes = letrasComunes(vocales,cons)
    mensaje = mensajeSalida(cons,letras_comunes)

    #salida
    print(mensaje)
