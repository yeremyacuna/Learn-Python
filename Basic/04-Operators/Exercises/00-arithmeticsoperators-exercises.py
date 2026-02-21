"""
Crea dos números a = 17 y b = 4 e imprime:

División normal

División entera

Módulo

Potencia a elevado a b
"""

a = 17 ; b = 4
print("Normal Division:", a/b)
print("Integer Division:", a//b)
print("Modulo:", a%b)
print("Exponentiation:",a**b,"\n")



"""
Determina si un número es par usando %.
"""

n = int(input("Insert a number: "))

if ((n % 2) == 0):
    print("par")
else:
    print("impar")