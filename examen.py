# 1. Funcion para registrar los datos basicos de los comercios
def registrar_comercios():
    comercios = []
    print("--- REGISTRO DE COMERCIOS ---")
    for i in range(10):
        print(f"\nDatos del comercio {i + 1}:")
        nit = input("NIT: ")
        nombre = input("Nombre comercial: ")
        tipo = input("Tipo (Tienda, Restaurante, Peluquería): ")
        empleados = int(input("Cantidad de empleados: "))
        meta_semanal = float(input("Meta máxima semanal (kWh): "))
        
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

# 2. Funcion para registrar las 4 mediciones semanales
def registrar_consumos(comercios):
    print("\n--- REGISTRO DE CONSUMOS SEMANALES ---")
    for comercio in comercios:
        print(f"\nIngresando consumos para: {comercio['nombre']}")
        for i in range(4):
            while True:
                consumo = float(input(f"Consumo de la semana {i + 1} (kWh): "))
                if consumo > 0:
                    comercio["consumos"].append(consumo)
                    break
                else:
                    print("Error: El consumo debe ser mayor que 0. Intenta de nuevo.")
    return comercios

# 3. Funcion para calcular el promedio
def calcular_promedio(consumos):
    suma = 0
    contador = 0
    for c in consumos:
        suma += c
        contador += 1
        
    if contador > 0:
        return suma / contador
    return 0

# 4. Funcion para calcular la variacion porcentual
def calcular_variacion(consumos):
    semana1 = consumos[0]
    semana4 = consumos[3]
    variacion = ((semana4 - semana1) / semana1) * 100
    return variacion

# 5. Funcion para clasificar el consumo del comercio
def clasificar_consumo(promedio, meta, variacion):
    # Limite superior del 20%
    limite_20_porciento = meta * 1.20 
    
    if promedio <= meta and variacion <= 5:
        return "Eficiente"
    elif promedio <= meta and variacion > 5:
        return "En observación"
    elif promedio > meta and promedio <= limite_20_porciento:
        return "Alto"
    else:
        return "Crítico"

# 6. Funcion para generar e imprimir el informe final
def generar_informe(comercios):
    eficientes = 0
    en_observacion = 0
    altos = 0
    criticos = 0
    
    # Variables para encontrar el mayor consumo manualmente
    mayor_promedio = -1
    nombre_mayor = ""
    
    print("\n" + "="*45)
    print(" INFORME FINAL DE CONSUMO ENERGÉTICO")
    print("="*45)
    
    for comercio in comercios:
        # Extraemos los datos pre-calculados desde la ejecucion principal
        prom = comercio["promedio"]
        var = comercio["variacion"]
        clasif = comercio["clasificacion"]
        
        # Conteo de clasificaciones
        if clasif == "Eficiente":
            eficientes += 1
        elif clasif == "En observación":
            en_observacion += 1
        elif clasif == "Alto":
            altos += 1
        elif clasif == "Crítico":
            criticos += 1
            
        if prom > mayor_promedio:
            mayor_promedio = prom
            nombre_mayor = comercio["nombre"]
            
        # Imprimir datos por comercio
        print(f"Comercio:      {comercio['nombre']}")
        print(f"Promedio:      {prom:.2f} kWh")
        print(f"Variación:     {var:.2f}%")
        print(f"Clasificación: {clasif}")
        print("-" * 45)
        
    print("\n--- RESUMEN GLOBAL ---")
    print(f"Eficiente:      {eficientes} comercios")
    print(f"En observación: {en_observacion} comercios")
    print(f"Alto:           {altos} comercios")
    print(f"Crítico:        {criticos} comercios")
    print(f"\n>> El comercio con el MAYOR promedio fue '{nombre_mayor}' con {mayor_promedio:.2f} kWh.")

# Ejecucion Principal (Main)
if __name__ == "__main__":
    lista_comercios = registrar_comercios()
    
    # 2. Registrar consumos
    lista_comercios = registrar_consumos(lista_comercios)

    for negocio in lista_comercios:
        # 3. Llamado a calcular promedio
        prom = calcular_promedio(negocio["consumos"])
        # 4. Llamado a calcular variación
        var = calcular_variacion(negocio["consumos"])
        # 5. Llamado a clasificar consumo
        clasif = clasificar_consumo(prom, negocio["meta_semanal"], var)
        
        # Almacenamos temporalmente en el diccionario para el informe
        negocio["promedio"] = prom
        negocio["variacion"] = var
        negocio["clasificacion"] = clasif
        
    # 6. Generar informe
    generar_informe(lista_comercios)