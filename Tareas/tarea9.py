def postulantes_a_lista(nombre_archivo):
    # 0id_postulación;1edad;2género;3nombre postulante;4fecha_inicio_trabajo;5salario_mensual
    # Variables
    archivo_postulantes = open(nombre_archivo)

    # Convertir archivo en lista
    lista_postulantes = []
    for linea in archivo_postulantes:
        linea = linea.strip()
        postulante = linea.split(';')
        lista_postulantes.append(postulante)

    archivo_postulantes.close()
    return lista_postulantes


def filtrar_postulantes(lista_postulantes):
    # Variables
    edad_minima = 18
    salario_maximo = 1140000

    # Filtrar postulantes que pueden optar al IFE laboral
    postulantes_filtrados = []
    for postulante in lista_postulantes:
        # Determinar si empezo a trabajar en una fecha valida
        fecha_valida = False
        fecha_inicio = postulante[4]
        fecha = fecha_inicio.split('-')
        if int(fecha[0]) == 2021 and int(fecha[1]) >= 7:
            fecha_valida = True
        elif int(fecha[0]) == 2022 and int(fecha[1]) <= 3:
            fecha_valida = True

        # Determinar si la edad y el salario estan dentros de los rangos permitidos
        edad = int(postulante[1])
        salario = int(postulante[5])
        if edad >= edad_minima and fecha_valida and salario <= salario_maximo:
            postulantes_filtrados.append(postulante)

    return postulantes_filtrados


def calcular_ife(beneficiarios):
    ife_beneficiarios = []
    for beneficiario in beneficiarios:
        # Variables
        edad = int(beneficiario[1])
        genero = beneficiario[2]
        nombre = beneficiario[3]
        salario = int(beneficiario[5])

        # En caso de ser mujer o ser hombre menor a 24 a;os o mayor a 55
        if genero == 'F' or edad <= 23 or edad > 55:
            ife_mensual = round(salario * 0.45)
            ife = ife_mensual * 3
            if ife > 1000000:
                ife = 1000000

        # En caso de ser hombre entre 24 y 55 a;os inclusive
        else:
            ife_mensual = round(salario * 0.35)
            ife = ife_mensual * 3
            if ife > 750000:
                ife = 750000

        ife_beneficiarios.append([ife, salario, nombre, edad])

    # Reordenar datos
    ife_beneficiarios.sort()
    ife_beneficiarios.reverse()
    for beneficiario in ife_beneficiarios:
        beneficiario.reverse()

    return ife_beneficiarios


def generar_archivo_rango(beneficiarios, min_inclusive, max_inclusive):
    # Variables
    cantidad_personas = 0
    ife_total = 0

    # Crear archivo
    archivo = open("resumen_{}_{}.txt".format(str(min_inclusive), str(max_inclusive)), 'w')

    # A;adir datos al archivo
    for beneficiario in beneficiarios:
        tmp = list(beneficiario)
        edad = int(tmp[0])
        if min_inclusive <= edad <= max_inclusive:
            # Datos para estadisticas
            cantidad_personas += 1
            ife_total += tmp[3]

            # Formatear texto para agregar a archivo
            tmp[2] = str(tmp[2])
            tmp[3] = str(tmp[3])
            del tmp[0]
            archivo.write(';'.join(tmp) + '\n')

    archivo.close()
    return [min_inclusive, max_inclusive, cantidad_personas, ife_total]

# Adquirir datos de postulantes, filtrar y calcular ife correspondiente
postulantes = postulantes_a_lista("postulantes.txt")
beneficiarios = filtrar_postulantes(postulantes)
ife_beneficiarios = calcular_ife(beneficiarios)

# Generar archivos resumen y adquirir datos para archivo estadisticas
estadisticas = []
rangos = open("rangos.txt")
edad_minima = 18
for linea in rangos:
    edad_maxima = int(linea)
    estadisticas_rango = generar_archivo_rango(ife_beneficiarios, edad_minima, edad_maxima)
    estadisticas.append(estadisticas_rango)
    edad_minima = edad_maxima + 1
estadisticas_rango = generar_archivo_rango(ife_beneficiarios, edad_minima, 65)
estadisticas.append(estadisticas_rango)
rangos.close()

# Generar archivo estadisticas
archivo_estadisticas = open("estadísticas.txt", 'w')
archivo_estadisticas.write("Resultado de la asignación del IFE\n")

# Totales
monto_total = 0
cantidad_beneficiarios = 0
for dato in estadisticas:
    monto_total += dato[3]
    cantidad_beneficiarios += dato[2]
archivo_estadisticas.write("Monto total asignado: ${}\n".format(monto_total))
archivo_estadisticas.write("Beneficiarios: {}\n\n".format(cantidad_beneficiarios))
archivo_estadisticas.write("Distribución por rangos de edad:\n\n")

# Datos por rangos dados
for dato in estadisticas:
    min_rango = dato[0]
    max_rango = dato[1]
    porcentaje_beneficiarios = round(dato[2] * 100 / cantidad_beneficiarios, 1)
    porcentaje_monto = round(dato[3] * 100 / monto_total, 2)
    archivo_estadisticas.write("Las personas entre {} y {} años representan un {}% del total de personas.\n".format(min_rango, max_rango, porcentaje_beneficiarios))
    archivo_estadisticas.write("La asignación para este rango corresponde a un {}% del monto total asignado.\n\n".format(porcentaje_monto))

archivo_estadisticas.close()
