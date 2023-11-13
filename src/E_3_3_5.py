#3.3.5

def pares(numeros,par):
    resultado = numeros & par
    resultado = list(map(int,resultado))
    return resultado

if __name__ == "__main__":

    #entrada
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    par = {2,4,6,8,10}
    multiplo_3 = {1,3,6,9}

    #proceso

    #salida
    print(pares(numeros,par))