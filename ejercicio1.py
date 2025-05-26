# -------> Ejercicio 1: Cálculo del valor de un terreno rectangular <-----
# Un municipio desea automatizar el cálculo del valor de terrenos rectangulares.

def calcular_valor_terreno():
    # Solicitar dimensiones del terreno
    largo_t = float(input("Ingrese el largo del terreno en metros: "))
    ancho_t = float(input("Ingrese el ancho del terreno en metros: "))

    # Solicitar el valor por metro cuadrado
    valor_metro = float(input("Ingrese valor del metro cuadrado en pesos: $ "))

    # Calcular área y valor total del terreno
    area_terreno = largo_t * ancho_t
    valor_terreno = area_terreno * valor_metro

    # Mostrar resultados
    print("El área del terreno es:", area_terreno, "Mt2")
    print("El precio total del terreno es: $", valor_terreno)
    
calcular_valor_terreno()
