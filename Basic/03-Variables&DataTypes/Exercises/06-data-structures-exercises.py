"""LISTA
Crea una lista con 5 números.

Imprime el tercero

Agrega un número al final

Elimina el segundo
"""

lista = [1,2,3,4,5]
print(lista[2])
lista.append(6)
print(lista)
lista.pop(1)
print(lista, "\n")

"""TUPLE
Crea una tupla con 3 colores.

Imprime el último

Intenta cambiar uno (mira qué pasa)
"""

colors = ("Orange", "Blue", "Pink")
print(colors, "\n"+ (colors[-1]), '\n')

#colors[2] = "Yellow" -> error : 'tuple' object does not support item assignment

"""SET
Crea un set con números repetidos:

1,2,2,3,4,4,5


Imprime el set

Agrega 10

Elimina 3
"""

numbers_duplicate = {1,2,2,3,4,4,5}
print(numbers_duplicate)

numbers_duplicate.add(10)
numbers_duplicate.remove(3)
print(numbers_duplicate)

"""DICTIONARY
Crea un diccionario:

name
age
country


Imprime solo el nombre

Cambia la edad

Agrega una nueva clave llamada "job"
"""

my_info = {
    "name": "Yeremy Acuña",
    "age": 18,
    "country" : "Peru"
}
print(my_info["name"])
my_info["age"] = 19

my_info["job"] = "Software Engineer"
print(my_info)