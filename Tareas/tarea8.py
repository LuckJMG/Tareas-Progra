def comunas_con_mas_oferta(lista, operacion):
    # Variables
    ofertas = {}
    comunas = []
    cantidades = []
    top_oferta = []
    top = 3

    # Contar cantidad de ofertas por tipo y comuna
    for oferta in lista:
        if oferta[2] == operacion:
            if oferta[3] not in ofertas:
                ofertas[oferta[3]] = 0
            ofertas[oferta[3]] += 1

    # Separar en listas
    for comuna in ofertas:
        comunas.append(comuna)
        cantidades.append(ofertas[comuna])

    # Calcular el top de ofertas
    while top > 0:
        # Variables
        cantidad = max(cantidades)
        indice = cantidades.index(cantidad)
        comuna = comunas[indice]

        top_oferta.append(comuna)

        del cantidades[indice]
        del comunas[indice]

        top -= 1

    return top_oferta


def filtrar(lista, tipo, operacion, min_dormitorios, min_m2):
    # Variables
    comunas = {}

    # Aplicar filtro
    for oferta in lista:
        # Variables
        formato = [oferta[10], oferta[0], oferta[4], oferta[5], oferta[6], oferta[7], oferta[8], oferta[9]]

        if oferta[1] == tipo and oferta[2] == operacion:
            if oferta[4] >= min_dormitorios and oferta[7] >= min_m2:
                if oferta[3] not in comunas:
                    comunas[oferta[3]] = []
                comunas[oferta[3]].append(formato)

    # Ordenar de menor a mayor
    for comuna in comunas:
        # Variables
        ofertas = comunas[comuna]

        if len(ofertas) > 1:
            precios = []
            lista_ordenada = []

            for oferta in ofertas:
                precios.append(oferta[0])
                lista_ordenada.append(oferta)

            contador = len(comunas[comuna])
            comunas[comuna] = []

            while contador > 0:
                indice = precios.index(min(precios))
                comunas[comuna].append(lista_ordenada[indice])
                del lista_ordenada[indice]
                del precios[indice]
                contador -= 1

    return comunas


def buscar(ofertas, solicitudes):
    # Variables
    resultados = []

    # Aplicar solicitud
    for solicitud in solicitudes:
        # Variables
        nombre = solicitud[0]
        filtro = solicitud[1]
        comunas = filtrar(ofertas, filtro[0], filtro[1], filtro[2], filtro[3])
        disponibles = []

        for comuna in comunas:
            disponibles.append([comuna] + comunas[comuna][0])

        resultados.append([nombre, disponibles])

    return resultados
