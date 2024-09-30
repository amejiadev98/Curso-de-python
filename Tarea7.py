#calcule el area de un triangulo
import math
 
def area_triangulo(base, altura):
    area = base * altura / 2
    return area
base = float(input("Introduzca la base del triangulo "))
altura = float(input("Introduzca la area del triangulo "))


area = area_triangulo(base, altura)
print(f"El area total de un triangulo es {area}")

