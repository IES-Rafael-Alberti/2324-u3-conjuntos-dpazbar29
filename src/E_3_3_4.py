#3.3.4


def Conjunto1(frutas1):
    set_frutas_1 = set(frutas1)
    return set_frutas_1

def Conjunto2(frutas2):
    set_frutas_2 = set(frutas2)
    return set_frutas_2

def FrutasComunes(set_frutas_1,set_frutas_2):
    res = set_frutas_1 & set_frutas_2
    return res

def unicosFrutas1(set_frutas_1,set_frutas_2):
    res = set_frutas_1 - set_frutas_2
    return res

def unicosFrutas2(set_frutas_1,set_frutas_2):
    res = set_frutas_2 - set_frutas_1
    return res

def mensajeSalida(set_frutas_1,set_frutas_2,frutas_comunes,frutas_solo_1,frutas_solo_2):
    mensaje = "De los conjuntos " + str(set_frutas_1) + " y " + str(set_frutas_2) + ", tienen las siguientes frutas iguales " + str(frutas_comunes) + "\nFrutas solo en conjunto 1: " + str(frutas_solo_1) + "\nFrutas solo en conjunto 2: " + str(frutas_solo_2)
    return mensaje
if __name__ == "__main__":

    #entrada
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
    
    #proceso
    set_frutas_1 = Conjunto1(frutas1)
    set_frutas_2 = Conjunto2(frutas2)
    frutas_comunes = FrutasComunes(set_frutas_1,set_frutas_2)
    frutas_solo_1 = unicosFrutas1(set_frutas_1,set_frutas_2)
    frutas_solo_2 = unicosFrutas2(set_frutas_1,set_frutas_2)
    mensaje = mensajeSalida(set_frutas_1,set_frutas_2,frutas_comunes,frutas_solo_1,frutas_solo_2)

    #salida
    print(mensaje)