#3.3.2

def nombresTotal(nombres_primaria,nombres_secundaria):
    resultado = nombres_primaria | nombres_secundaria
    strResultado = ",".join(resultado)
    return strResultado

def nombresRepetidos(nombres_primaria,nombres_secundaria):
    resultado = nombres_primaria & nombres_secundaria
    if resultado == set():
        resultado = "No hay nombres repetidos en ambos grados"
    else:
        strResultado = ",".join(resultado)
    return strResultado

def PrimariaNoRepetidoSecudanria(nombres_primaria,nombres_secundaria):
    resultado = nombres_primaria - nombres_secundaria
    if resultado == set():
        resultado = "No hay nombres repetidos en ambos grados"
    return resultado

def PrimariaEnSecundaria(nombres_primaria,nombres_secundaria):
    resultado = nombres_primaria <= nombres_secundaria
    if resultado == True:
        salida = "Los nombres de primaria están incluidos en secundaria"
    else:
        salida = "Los nombres de primaria no están incluidos en secundaria"
    return salida

def mensajeSalida(nombres_sin_repetir,nombres_repetidos,nombres_primaria_secundaria,nombres_primaria_incluidos_secundaria):
    mensaje = "Nombres totales: " + str(nombres_sin_repetir) + "\nNombres repetidos: " + str(nombres_repetidos) + "\nNombres primaria no repetidos en secundaria: " + str(nombres_primaria_secundaria) + "\nNombres primaria incluidos en secundaria: " + str(nombres_primaria_incluidos_secundaria)
    return mensaje

if __name__ ==  "__main__":

    #entrada
    nombres_primaria = []
    nombres_primaria = set(nombres_primaria)
    nombres_secundaria = []
    nombres_secundaria = set(nombres_secundaria)
    interruptor_primaria = True
    interruptor_secundaria = True

    while interruptor_primaria == True:
        nombre_primaria = input("Introduce el nombre de un alumno de primaria(x para terminar): ")
        if nombre_primaria == "" or nombre_primaria == " ":
            nombres_primaria.pop()
        elif nombre_primaria != "x":
            nombres_primaria.add(nombre_primaria)
        else:
            interruptor_primaria = False
    
    while interruptor_secundaria == True:
        nombre_secundaria = str(input("Introduce el nombre de un alumno de secundaria(x para terminar): ")) 
        if nombre_primaria == "" or nombre_primaria == " ":
            nombres_primaria.pop()
        if nombre_secundaria != "x":
            nombres_secundaria.add(nombre_secundaria)
        else:
            interruptor_secundaria = False

    #proceso
    nombres_sin_repetir = nombresTotal(nombres_primaria,nombres_secundaria)
    nombres_repetidos = nombresRepetidos(nombres_primaria,nombres_secundaria)
    nombres_primaria_secundaria = PrimariaNoRepetidoSecudanria(nombres_primaria,nombres_secundaria)
    nombres_primaria_incluidos_secundaria  = PrimariaEnSecundaria(nombres_primaria,nombres_secundaria)
    mensaje = mensajeSalida(nombres_sin_repetir,nombres_repetidos,nombres_primaria_secundaria,nombres_primaria_incluidos_secundaria) 

    #salida
    print(mensaje)