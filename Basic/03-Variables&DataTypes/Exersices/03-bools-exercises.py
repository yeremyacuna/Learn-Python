"""
Evalúa:

10 > 5

3 == 7

not False

True and False

True or False

5 != 5

7 >= 7
"""

print(10>5, 3==7, not False, True and False, True or False, 5!=5, 7>=7)

"""
Convierte a boolean:

0
1
""
"Python"
[]
[1,2,3]
None

"""

print(bool(0), bool(1),bool(""), bool("Python"), bool([]), bool([1,2,3]), bool(None))

"""
age= 18
Crea variable que sea True si es mayor o igual a 18.
"""

age = 18

if age >= 18:
    verdadero = True
    print(verdadero)

if verdadero:
    print("Si es mayor")

"""
x = 10
y = 20

Expresión que sea True solo si:

x < y
y > 15
x != 5
"""

x=10;y=20

result = (x < y) and (y > 15) and (x != 5)
print(result)