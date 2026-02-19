"""
Crea dos variables a = 15 y b = 4.
Imprime:

La suma

La resta

La multiplicación

La división normal

La división entera

El módulo

Eleva 7 a la potencia 4.

Convierte el string "25" en entero y súmale 10.
"""

a = 15; b = 4
print("The addition is:", a + b )
print("The subtraction is:", a-b)
print("The multiplication is",a*b)
print("The division is:", a/b)
print("The interger division is", a//b)
print("The modulus is:", a%b)
print("The exponentiation is:", 7**4)

string_to_int = '25'
print(10 + int(string_to_int))


print('\n')


"""
Dado un número entero n = 1234, imprime el último dígito.

"""

n = 1234
print(n%10)

"""
Dado n = 987, imprime la suma de sus dígitos.
"""

#1
n = 987
suma  = 0
d1 = n%10 #7
d3 = int(n/100) #9
d2 = int((n - d3*100) // 10)
suma = d1+d2+d3
print(suma)

#2

suma = 0
while n>0:
    suma += n%10
    n//=10

print(suma)