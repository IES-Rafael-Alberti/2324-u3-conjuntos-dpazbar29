#3.3.5

def pares(numeros):
    par = {}
    par = set()
    for i in range(0,len(numeros)+1):
        if i % 2 == 0:
            par.add(i)
    return par

def multiplosTres(numeros):
    multiplos_de_tres = {}
    multiplos_de_tres  = set()
    for i in range(1,len(numeros)+1):
        if i % 3 == 0:
            multiplos_de_tres.add(i)
    return multiplos_de_tres

def interseccionParesMultiplosTres(par,multiplos_de_tres):
    resultado = par & multiplos_de_tres
    return resultado

def mensajeSalida(par,multiplos_de_tres,interseccion):
    mensaje = "Lo numeros pares son: " + str(par) + "\nNumeros impares: " + str(multiplos_de_tres) + "\nNumeros pares y múltiplos de 3 coincidentes: " + str(interseccion)
    return mensaje

if __name__ == "__main__":

    #entrada
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    #proceso
    par = pares(numeros)
    multiplos_de_tres = multiplosTres(numeros)
    interseccion = interseccionParesMultiplosTres(par,multiplos_de_tres)
    mensaje = mensajeSalida(par,multiplos_de_tres,interseccion)

    #salida
    print(mensaje)