"""
File: operators.py
Description: Demonstrates arithmetic, comparison, logical,
assignment, membership and identity operators in Python.
Author: Yeremy
"""

# ----------------------------------------
# Arithmetic operators
# ----------------------------------------

a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Integer Division:", a // b)
print("Modulo:", a % b)
print("Power:", a ** b)

# ----------------------------------------
# Comparison operators
# ----------------------------------------

print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater:", a > b)
print("Less:", a < b)
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b)

# ----------------------------------------
# Logical operators
# ----------------------------------------

age = 21
has_id = True
registered = True

can_enter = age >= 18 and has_id and registered
print("Can enter:", can_enter)

# ----------------------------------------
# Assignment operators
# ----------------------------------------

counter = 0
counter += 5
counter *= 2
counter -= 3
print("Counter:", counter)

# ----------------------------------------
# Membership operators
# ----------------------------------------

word = "programming"
print("'g' in word:", "g" in word)
print("'z' not in word:", "z" not in word)

# ----------------------------------------
# Identity operators
# ----------------------------------------

list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print("list_a is list_b:", list_a is list_b)
print("list_a is list_c:", list_a is list_c)
print("list_a == list_c:", list_a == list_c)

# ----------------------------------------
# End of program
# ----------------------------------------
