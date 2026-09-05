Actua como un tutor experto en Python y ayudame a resolver el siguiente reto de programacion. Es indispensable que el codigo cumpla con todas las restricciones tecnicas: no puedes usar librerias externas, clases, ni funciones integradas como sum(), max() o min(). Los calculos estadisticos deben hacerse manualmente con ciclos. Ademas, el programa debe estructurarse obligatoriamente en 6 funciones especificas, las cuales deben ser invocadas en el bloque principal de ejecucion.

Aqui esta el detalle del ejercicio:

Sistema de monitoreo de consumo energetico en pequenos comercios

Contexto:
Una empresa de asesoria energetica acompana pequenos comercios de barrio para identificar consumos elevados de electricidad. Durante una visita se registra informacion basica de cada negocio y cuatro mediciones semanales de consumo. Se necesita un prototipo que permita organizar los datos, calcular indicadores sencillos y detectar comercios que deberian recibir una recomendacion de ahorro.

Reto:
Desarrolle un programa en Python que resuelva el caso planteado. La solucion debe estar dividida en exactamente 6 funciones principales:

registrar_comercios(): Registra 10 comercios con sus datos basicos en diccionarios y retorna la lista.

registrar_consumos(comercios): Solicita 4 consumos semanales mayores a 0 para cada comercio.

calcular_promedio(consumos): Calcula el promedio manualmente con un ciclo y acumulador.

calcular_variacion(consumos): Calcula la diferencia porcentual entre la semana 1 y la 4.

clasificar_consumo(promedio, meta, variacion): Eficiente si promedio <= meta y variacion <= 5%; En observacion si promedio <= meta pero variacion > 5%; Alto si promedio > meta hasta un 20%; Critico si supera la meta en mas del 20%. Retorna la clasificacion.

generar_informe(comercios): Mostrar por comercio: nombre, promedio, variacion y clasificacio. Al final indicar cuantos comercios estan en cada clasificacion y cual tuvo el mayor promedio, hallandolo con un ciclo y comparaciones.
