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


def principal():
    # Variables
    nombre_cliente = ""
    monto_prestado = 0
    plazo = 0
    valor_mensual = 0
    valor_total = 0
    
    # Encabezado del programa
    print("=" * 70)
    print("💰 SIMULADOR DE PRESTAMOS BANCARIOS".center(70))
    print("=" * 70)
    print("\n")
    
    # Preguntar el nombre del cliente
    while True:
        nombre_cliente = input("Nombre del cliente: ")
        if nombre_cliente != "":
            break
        else:
            print("El nombre no puede estar vacío")
    
    # Preguntar el monto prestado
    while True:
        monto_prestado = int(input("Monto prestado: "))
        if monto_prestado >= 1000000 and monto_prestado <= 50000000:
            break
        else:
            print("El monto prestado debe estar entre $1,000,000 y $50,000,000")
    
    # Preguntar el plazo
    while True:
        plazo = int(input("Plazo (6, 12 o 24 meses): "))
        if plazo == 6 or plazo == 12 or plazo == 24:
            break
        else:
            print("El plazo debe ser 6, 12 o 24 meses")
    
    # Calcular el valor mensual a pagar
    if plazo == 6:
        valor_mensual = monto_prestado * 0.015
    elif plazo == 12:
        valor_mensual = monto_prestado * 0.013
    else:
        valor_mensual = monto_prestado * 0.011
    
    # Calcular el valor total a pagar
    valor_total = valor_mensual * 12
    
    # Mostrar el resumen
    print("=" * 70)
    print("📊 RESUMEN".center(70))
    print("=" * 70)
    print("\n")
    print(f"Nombre: {nombre_cliente}")
    print(f"Monto prestado: {monto_prestado:,.0f} €")
    print(f"Plazo: {plazo} meses")
    print(f"Valor mensual a pagar: {valor_mensual:,.0f} €")
    print(f"Valor total a pagar: {valor_total:,.0f} €")
    
    
principal()