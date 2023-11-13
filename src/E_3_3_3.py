#3.3.3
def sacarNumerosIndividualmente(conjunto):
    resultado = []
    for i in conjunto:
        resultado.append(i)
    return resultado

if __name__ == "__main__": 

    #entrada
    conjunto = {3,2,1}

    #proceso
    numeros_individuales = sacarNumerosIndividualmente(conjunto)

    #salida
    print(numeros_individuales)

