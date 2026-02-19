"""
Crea dos floats:

x = 5.5
y = 2.3


Imprime:

Suma

Resta

Multiplicación

División

División entera

Módulo

Potencia (x elevado a y)
"""

x = 5.5; y=2.3
print("The addition is:", x + y)
print("The subtraction is:", x-y)
print("The multiplication is:", x*y)
print("The division is:", x/y)
print("The integer division is:", int(x//y))
print("The modulus is:" , x%y)
print("The exponentiation is", x**y)

"""
Convierte el entero 8 en float y luego:

Multiplícalo por 2.5

Imprime el tipo de dato usando type()
"""

int_float = 8
print(type(int_float))
print(float(int_float)*2.5)
print(type(float(int_float)*2.5))

"""
Calcula el área de un círculo:

radio = 3.5

Usa math.pi

Fórmula: πr**2
"""

import math

radio = 3.5
print(radio**2*math.pi) 

"""
num = 3.1415926535
Redondea a 3 decimales

Redondea hacia arriba

Redondea hacia abajo

"""

num = 3.1415926535
print(round(num,3)) ##Redondeo
print(math.ceil(num)) ##Hacia Arriba
print(math.floor(num)) ##Hacia Abajo