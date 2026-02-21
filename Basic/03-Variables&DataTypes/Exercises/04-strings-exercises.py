"""
text = "Python Programming"


Imprime:

Primera letra

Última letra

Primeros 6 caracteres

Desde posición 7 hasta el final

Invertido
"""

text = "Python Programming"

print(text[0])
print(text[-1])
print(text[0:6])
print(text[7:])
print(text[::-1])

"""
Une:

a = "Hello"
b = "World"


Con espacio.
"""

a="Hello"
b="World"; print(a+" "+b)

"""
text = "   I love Python   "


Quita espacios

Pasa a mayúsculas

Reemplaza "Python" por "Backend"

Cuenta caracteres sin espacios

"""
text = "   I love Python   "
text = text.strip()

print(text.upper())
print(text.replace("Python", "Backend"))
print(len(text)-2); print(len(text.replace(" ", "")))

"""
sentence = "Python is powerful and easy"


Divide en palabras

Cuenta cuántas

Únelas con "-"
"""

sentence = "Python is powerful and easy"
sentence = sentence.split()
print(sentence)
print(len(sentence))
sentence = "-".join(sentence)
print(sentence)

"""
Usa f-string:

My name is ___ and I am ___ years old.
"""

age = 18; name = "Yeremy"
print(f"My name is {name} and I am {age} years old")