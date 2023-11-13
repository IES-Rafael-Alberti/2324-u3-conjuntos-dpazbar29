#3.3.1
def obtenerDomiciliosFacturas(compras):
    domicilios_facturas = set()
    clientes_domicilios = {}

    for compra in compras:
        cliente, dia_del_mes, monto, domicilio = compra

        if cliente not in clientes_domicilios:
            clientes_domicilios[cliente] = set()

        clientes_domicilios[cliente].add(domicilio)

    for domicilios in clientes_domicilios.values():
        domicilios_facturas.update(domicilios)

    return list(domicilios_facturas)

if __name__ == "__main__":

    #entrada
    compras = [
    ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
    ("Jorge Russo", 7, 699, "Mirasol 218"),
    ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
    ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
    ("Jorge Russo", 15, 958, "Mirasol 218")
    ]

    #proceso
    domicilios_para_facturas = obtenerDomiciliosFacturas(compras)

    #salida
    print(domicilios_para_facturas)
