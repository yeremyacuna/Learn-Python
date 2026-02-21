"""
Crea un contador que:

Empiece en 10

Sume 5

Se multiplique por 3

Reste 8

Se divida entre 2
Imprime resultado final.
"""

cont = 10
cont += 5
cont *= 3
cont -= 8
cont /= 2

print(cont, "\n")

"""
Usa //= y %= con números negativos.
Analiza qué pasa.
"""

negativeNumber = -8
negativeNumber //= -2
print(negativeNumber)
negativeNumber %= -3
print(negativeNumber)