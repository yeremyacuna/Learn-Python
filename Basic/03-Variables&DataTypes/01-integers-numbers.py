#### Variables and Data Types in Python

'''      ============= Integers numbers ================     '''
a = 10
b = -5
c = 0
print(a, b, c)

#1 Integers support arithmetic operations.
x = 7
y = 3

print("Addition:", x + y) # 10
print("Substraction:", x - y) # 4
print("Multiplication:", x * y) # 21
print("Division:", x / y) # 2.333... (always float)
print("Floor Division:", x // y) # 2 (integer division)
print("Modulo:", x % y) # 1 (remainder)
print("Exponentiation:", x ** y) # 343 (7^3)

#2 Integers can be converted from other types using int().
f = 3.9
s = "15"
print(int(f)) # 3, drops decimal
print(int(s)) # 15, converts from string

#3 Integers can be used in built-in functions.
nums = [1, 5, 3, 9, 2]
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))
print("Absolute:", abs(-10))