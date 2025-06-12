# -------> Taller 2, Ejercicio 2: Simulador de préstamos bancarios <-----
# Un banco simula préstamos a clientes. El sistema debe:
# 1. Preguntar el nombre del cliente
# 2. Preguntar cuánto desea pedir prestado(entre $1, 000, 000 y $50, 000, 000)
# 3. Elegir un plazo: 6, 12 o 24 meses
# Según el plazo, el interés es:
# • 6 meses: 1.5 % mensual
# • 12 meses: 1.3 % mensual
# • 24 meses: 1.1 % mensual
# Calcular:
# • Valor mensual a pagar
# • Valor total a pagar al final
# • Mostrar un resumen con los datos del cliente


def obtener_tasa_interes(plazo: int) -> float:
    if plazo == 6:
        return 0.015
    elif plazo == 12:
        return 0.013
    else:
        return 0.011


def calcular_valor_total(monto_prestado: int, plazo: int, tasa: float) -> float:
    interes_total = monto_prestado * tasa * plazo
    valor_total = monto_prestado + interes_total
    return valor_total


def principal() -> None:
    print("=" * 70)
    print("💰 SIMULADOR DE PRÉSTAMOS BANCARIOS".center(70))
    print("=" * 70)
    print("\n")

    # 1. Nombre del cliente
    while True:
        nombre_cliente: str = input("Nombre del cliente: ")
        if nombre_cliente.strip():
            break
        else:
            print("El nombre no puede estar vacío.")

    # 2. Monto a prestar
    while True:
        monto_prestado: int = int(input("Monto prestado: "))
        if 1000000 <= monto_prestado <= 50000000:
            break
        else:
            print("El monto debe estar entre $1'000,000 y $50'000,000.")

    # 3. Plazo
    while True:
        plazo: int = int(input("Plazo (6, 12 o 24 meses): "))
        if plazo in [6, 12, 24]:
            break
        else:
            print("El plazo debe ser 6, 12 o 24 meses.")

    # 4. Cálculos
    tasa = obtener_tasa_interes(plazo)
    valor_total = calcular_valor_total(monto_prestado, plazo, tasa)
    valor_mensual = valor_total / plazo

    # 5. Mostrar resumen
    print("\n" + "=" * 70)
    print("📊 RESUMEN".center(70))
    print("=" * 70)
    print("\n")
    print(f"Nombre del cliente: {nombre_cliente}")
    print(f"Monto prestado: ${monto_prestado:,.0f}")
    print(f"Plazo: {plazo} meses")
    print(f"Tasa de interés mensual: {tasa * 100:.1f}%")
    print(f"Valor mensual a pagar: ${valor_mensual:,.0f}")
    print(f"Valor total a pagar: ${valor_total:,.0f}")


principal()
