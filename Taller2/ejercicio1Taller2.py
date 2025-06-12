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

def calcular_pago(consumo: float) -> float:
    if consumo <= 15:
        return consumo * 2000
    elif consumo <= 30:
        return consumo * 2500
    else:
        return consumo * 3000


def principal() -> None:
    total_consumo = 0

    lista_nombres: str = ""
    lista_consumo: str = ""
    lista_valor_a_pagar: str = ""

    width_1: int = 80
    width_2: int = 40

    lineas_encabezado_1: str = "=" * width_1
    lineas_encabezado_2: str = "=" * width_2

    # Encabezado del programa
    print("\n" + f"{lineas_encabezado_1}")
    print("🧮 SIMULADOR DE PAGOS POR CONSUMO DE AGUA".center(width_1))
    print(f"{lineas_encabezado_1}" + "\n")

    total_apartamentos: int = int(
        input("Ingrese el número de apartamentos a evaluar: "))

    # Registro y cálculo por apartamento
    for i in range(0, total_apartamentos, 1):
        print("\n" + f"{lineas_encabezado_2}")
        print(f"Apartamento N.º {i + 1}".center(width_2))
        print(f"{lineas_encabezado_2}")

        nombre_residente: str = input("Nombre del residente: ")
        consumo_m3: float = float(input("Consumo en metros cúbicos: "))
        pago: float = calcular_pago(consumo_m3)

        total_consumo += consumo_m3

        lista_nombres += nombre_residente + ", "
        lista_consumo += f"{consumo_m3:.2f}, "
        lista_valor_a_pagar += f"${pago:,.0f}, "

    promedio: float = total_consumo / total_apartamentos

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
