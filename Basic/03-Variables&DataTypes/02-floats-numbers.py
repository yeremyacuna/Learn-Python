#### Variables and Data Types in Python

''' ============= Floats numbers ================ '''
f1 = 3.14
f2 = -0.001
f3 = 2.0 # floats can also be whole numbers with .0
print(f1, f2, f3)

#1 Floats support arithmetic operations.
x = 5.5
y = 2.0

print("Addition:", x + y) # 7.5
print("Substraction:", x - y) # 3.5
print("Multiplication:", x * y) # 11.0
print("Division:", x / y) # 2.75
print("Floor Division:", x // y) # 2.0
print("Modulo:", x % y) # 1.5
print("Exponentiation:", x ** y) # 30.25

#2 Floats can be converted from other types using float().
i = 7
s = "3.5"
print(float(i)) # 7.0
print(float(s)) # 3.5

#3 Floats can be used with math module for more functions.
import math

print("Square root:", math.sqrt(16)) # 4.0
print("Ceiling:", math.ceil(3.2)) # 4
print("Floor:", math.floor(3.8)) # 3
print("Pi value:", math.pi) # 3.141592653589793
print("Exponential e^2:", math.exp(2)) # 7.38905609893065
print("Logarithm ln(7):", math.log(7)) # 1.9459101490553132

#4 Mixing integers and floats
a = 5 # int
b = 2.5 # float
c = a + b # result is float
print("Mixing int + float:", c) # 7.5

#5 Comparison operations
x = 7
y = 3.5
print("x > y:", x > y) # True
print("x < y:", x < y) # False
print("x == y:", x == y) # False
print("x != y:", x != y) # True