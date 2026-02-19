"""
File: variables_all_types.py
Description: Demonstrates all main data types in Python in a detailed and professional way.
Author: Yeremy
"""

# ----------------------------------------
# Numeric types
# ----------------------------------------

integer_num = 10           # int
decimal_num = 3.14         # float
complex_num = 2 + 3j       # complex

print("Integer:", integer_num)
print("Float:", decimal_num)
print("Complex:", complex_num)
print("Complex real part:", complex_num.real)
print("Complex imag part:", complex_num.imag)

# ----------------------------------------
# Boolean type
# ----------------------------------------

is_student = True          # bool
has_graduated = False     # bool

print("Is student:", is_student)
print("Has graduated:", has_graduated)

# ----------------------------------------
# String type
# ----------------------------------------

name = "Yeremy"            # str
greeting = 'Hello'         # str

print("Name:", name)
print("Greeting:", greeting)

# ----------------------------------------
# List (ordered, mutable)
# ----------------------------------------

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")    # Add element

print("Fruits:", fruits)
print("First fruit:", fruits[0])

# ----------------------------------------
# Tuple (ordered, immutable)
# ----------------------------------------

coordinates = (10, 20)
print("Coordinates:", coordinates)
# coordinates[0] = 5       # ❌ This would raise an error

# ----------------------------------------
# Set (unordered, unique elements)
# ----------------------------------------

colors = {"red", "green", "blue", "red"}  # Duplicate 'red' ignored
print("Colors set:", colors)

# ----------------------------------------
# Dictionary (key-value pairs)
# ----------------------------------------

person = {"name": "Yeremy", "age": 18}
print("Person name:", person["name"])
person["age"] = 19  # Update value
print("Person age:", person["age"])

# ----------------------------------------
# Type checking
# ----------------------------------------

variables = [integer_num, decimal_num, complex_num, is_student, name, fruits, coordinates, colors, person]

for var in variables:
    print(f"Type of {var}:", type(var))

# ----------------------------------------
# Type casting examples
# ----------------------------------------

age_str = str(integer_num)        # int -> str
age_float = float(integer_num)    # int -> float

print("Age as string:", age_str)
print("Age as float:", age_float)

# ----------------------------------------
# End of program
# ----------------------------------------