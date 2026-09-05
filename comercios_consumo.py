def registrar_comercios():
    comercios = []

    for i in range(10):
        print(f"\n--- Registro del comercio {i + 1} ---")
        nit = input("NIT: ")
        nombre = input("Nombre: ")
        tipo = input("Tipo (Tienda, Restaurante, Peluquería): ")

        empleados = None
        while empleados is None:
            entrada = input("Número de empleados: ")
            try:
                empleados = int(entrada)
            except ValueError:
                print("Debes ingresar un número entero. Intenta de nuevo.")

        meta_semanal = None
        while meta_semanal is None:
            entrada = input("Meta semanal de consumo (kWh): ")
            try:
                meta_semanal = float(entrada)
            except ValueError:
                print("Debes ingresar un número. Intenta de nuevo.")

        comercio = {
            "nit": nit,
            "nombre": nombre,
            "tipo": tipo,
            "empleados": empleados,
            "meta_semanal": meta_semanal,
            "consumos": []
        }

        comercios.append(comercio)

    return comercios


def registrar_consumos(comercios):
    for comercio in comercios:
        print(f"\n--- Consumos semanales de {comercio['nombre']} ---")
        consumos_comercio = []

        for semana in range(4):
            valor = None
            while valor is None:
                entrada = input(f"Consumo semana {semana + 1} (kWh): ")
                try:
                    valor = float(entrada)
                    if valor <= 0:
                        print("El consumo debe ser mayor que 0. Intenta de nuevo.")
                        valor = None
                except ValueError:
                    print("Debes ingresar un número. Intenta de nuevo.")

            consumos_comercio.append(valor)

        comercio["consumos"] = consumos_comercio

    return comercios


def calcular_promedio(consumos):
    suma = 0

    for valor in consumos:
        suma = suma + valor

    promedio = suma / len(consumos)
    return promedio


def calcular_variacion(consumos):
    semana1 = consumos[0]
    semana4 = consumos[3]

    variacion = ((semana4 - semana1) / semana1) * 100
    return variacion


def clasificar_consumo(promedio, meta, variacion):
    if promedio <= meta and variacion <= 5:
        clasificacion = "Eficiente"
    elif promedio <= meta and variacion > 5:
        clasificacion = "En observación"
    elif promedio > meta and promedio <= meta * 1.20:
        clasificacion = "Alto"
    else:
        clasificacion = "Crítico"

    return clasificacion


def generar_informe(comercios):
    contador_eficiente = 0
    contador_observacion = 0
    contador_alto = 0
    contador_critico = 0

    mejor_promedio = 0
    nombre_mejor_promedio = ""

    print("\n===== INFORME DE CONSUMO ELÉCTRICO =====")

    for comercio in comercios:
        promedio = calcular_promedio(comercio["consumos"])
        variacion = calcular_variacion(comercio["consumos"])
        clasificacion = clasificar_consumo(promedio, comercio["meta_semanal"], variacion)

        print(f"\nComercio: {comercio['nombre']}")
        print(f"  Promedio: {promedio:.2f} kWh")
        print(f"  Variación: {variacion:.2f}%")
        print(f"  Clasificación: {clasificacion}")

        if clasificacion == "Eficiente":
            contador_eficiente += 1
        elif clasificacion == "En observación":
            contador_observacion += 1
        elif clasificacion == "Alto":
            contador_alto += 1
        else:
            contador_critico += 1

        if promedio > mejor_promedio:
            mejor_promedio = promedio
            nombre_mejor_promedio = comercio["nombre"]

    print("\n===== RESUMEN GENERAL =====")
    print(f"Eficiente: {contador_eficiente}")
    print(f"En observación: {contador_observacion}")
    print(f"Alto: {contador_alto}")
    print(f"Crítico: {contador_critico}")

    print(f"\nComercio con el mayor consumo promedio: {nombre_mejor_promedio} "
          f"({mejor_promedio:.2f} kWh)")


def main():
    comercios = registrar_comercios()
    comercios = registrar_consumos(comercios)
    generar_informe(comercios)


if __name__ == "__main__":
    main()