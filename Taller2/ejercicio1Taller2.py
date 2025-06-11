# -------> Taller 2, Ejercicio 1: Simulador de pagos por consumo de agua <-----
# En un edificio, se debe calcular el pago mensual por consumo de agua de cada apartamento.
# El usuario ingresa la cantidad de apartamentos.
# Por cada uno, registra:
# • Nombre del residente
# • Consumo en metros cúbicos
# El valor a pagar se calcula así:
# • Hasta 15 m³: $2000 por m³
# • Entre 16 y 30 m³: $2500 por m³
# • Más de 30 m³: $3000 por m³
# Al final, muestra:
# • Lista con nombres, consumo y valor a pagar
# • Total de agua consumida
# • Promedio de consume

def calcular_pago(consumo):
    if consumo <= 15:
        return consumo * 2000
    elif consumo <= 30:
        return consumo * 2500
    else:
        return consumo * 3000


def principal():
    total_consumo = 0

    lista_nombres = ""
    lista_consumo = ""
    lista_valor_a_pagar = ""
    
    width_1 = 70
    width_2 = 40
    
    lineas_encabezado_1 = "=" * width_1
    lineas_encabezado_2 = "=" * width_2

    # Encabezado del programa
    print("\n" + f"{lineas_encabezado_1}")
    print("🧮 SIMULADOR DE PAGOS POR CONSUMO DE AGUA".center(width_1))
    print(f"{lineas_encabezado_1}" + "\n")

    total_apartamentos = int(
        input("Ingrese el número de apartamentos a evaluar: "))

    # Registro y cálculo por apartamento
    for i in range(total_apartamentos):
        print("\n" + f"{lineas_encabezado_2}")
        print(f"Apartamento N.º {i + 1}".center(width_2))
        print(f"{lineas_encabezado_2}")

        nombre = input("Nombre del residente: ")
        consumo = float(input("Consumo en metros cúbicos: "))
        pago = calcular_pago(consumo)

        total_consumo += consumo

        lista_nombres += nombre + ", "
        lista_consumo += f"{consumo:.2f}, "
        lista_valor_a_pagar += f"${pago:,.0f}, "

    promedio = total_consumo / total_apartamentos

    # Resultados finales
    print("\n" + f"{lineas_encabezado_1}")
    print("📊 RESULTADOS FINALES".center(width_1))
    print(f"{lineas_encabezado_1}")

    print("\n📋 Tabla de resultados:\n")

    for i in range(total_apartamentos):
        print(f"🏠 Apartamento {i + 1}")
        print(f"   Nombre:          {lista_nombres.split(', ')[i]}")
        print(f"   Consumo:         {lista_consumo.split(', ')[i]} m³")
        print(f"   Valor a pagar:   {lista_valor_a_pagar.split(', ')[i]}")
        print(f"{lineas_encabezado_2}")

    print(f"\n💧 Total de agua consumida: {total_consumo:.2f} m³")
    print(f"📈 Promedio de consumo:     {promedio:.2f} m³\n")


# Ejecutar el programa
principal()
