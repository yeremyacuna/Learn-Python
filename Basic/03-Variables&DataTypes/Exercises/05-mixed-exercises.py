"""
Crea:

name (str)

age (int)

height (float)

is_adult (bool)

Imprime todo con f-string.
"""

name = 'Yeremy'
age= 18
height = 1.71
is_adult = age>=18

print(f"""Your name is: {name}, 
Your age is: {age},
Your height is: {height},
Are you an adult?: {is_adult}""")

"""
Crea un número complejo y guarda en boolean si su parte real > 5.
"""

complejonumber = 6j+99
real_complejonumber = complejonumber.real
bool_is_complex = real_complejonumber > 5; print("Its real number is "+ str(real_complejonumber) + " this is " + str(bool_is_complex) + " about Real > 5")

"""
value = "100.5"


Convierte a float

Súmale 20

Guarda boolean si > 150
"""

value = "100.5"
value = float(value)
print(value+20)
if_true = (value+20 > 150)
print(f"This is {if_true}")