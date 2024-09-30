#determine calcule el area de un circulo
import math

def calcular_circulo(radio):
    area = math.pi * radio**2
    return area

radio = float(input("Ingrese el radio del circulo "))
area= calcular_circulo(radio)
print(f"El area total del circulo {area}")

