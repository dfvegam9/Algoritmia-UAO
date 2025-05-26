# -------> Ejercicio 2: Conversión de grados Celsius a Fahrenheit <-----
# Realiza un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit. 
# Utiliza la fórmula: F = C × 9/5 + 32

def convertir_celsius_a_fahrenheit():
    # Se solicita la temperatura en Celsius
    temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    
    # Se calcula la temperatura en Fahrenheit
    temperatura_fahrenheit = temperatura_celsius * (9/5) + 32
    
    # Se muestra al usuario el resultado
    print(temperatura_celsius, "grados Celsius equivalen a", temperatura_fahrenheit, "grados Fahrenheit.")
    
convertir_celsius_a_fahrenheit()
