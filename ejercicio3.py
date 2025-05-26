# -------> Ejercicio 3: Cálculo del promedio de tres notas <-----
# Una escuela necesita calcular el promedio de tres notas para un estudiante.

def calcular_promedio():
    # Se solicita la info al usuario
    primera_nota = float(input("Ingrese la primera nota: "))
    segunda_nota = float(input("Ingrese la segunda nota: "))
    tercera_nota = float(input("Ingrese la tercera nota: "))

    # Se realiza el proceso
    promedio = (primera_nota + segunda_nota + tercera_nota) / 3

    # Se redondea a dos decimales
    promedio = int(promedio * 100) / 100

    # Se muestra al usuario el resultado con un mensaje claro
    print("El promedio de las tres notas del estudiante es:", promedio)

calcular_promedio()
