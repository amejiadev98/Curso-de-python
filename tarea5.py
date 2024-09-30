#Determine la hipotenusa de 2 catetos, dado los catetos
import math

def calcular_hipotenusa(cateto1, cateto2):
    hipotenusa= math.sqrt(cateto1**2 + cateto2**2)
    return hipotenusa

cateto1 = float(input("ingrese el primer valor de la hipotenusa "))
cateto2 = float(input("ingrese el segundo valor de la hipotenusa "))


hipotenusa = calcular_hipotenusa(cateto1, cateto2)
print(f"la hipotenusa es {hipotenusa}")

