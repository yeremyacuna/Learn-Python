#### Variables and Data Types in Python

'''      ============= Complex numbers ================     '''
z1 = 2 + 20j 
z2 = 5 - 2j
print(z1, z2) 


#1 Complex numbers can also be created using the complex() function.
z3 = complex(4, -5)  # 4 - 5j
print(z3)

#2 Complex numbers have real and imaginary parts, we can acces them using the .real and .imag attributes.
z = 7 + 8j
print("Real:", z.real) # Real part of 7.0
print("Imaginary:", z.imag) # Imaginary part of 8.0

#3 Complex numbers support arithmetic operations.
z = 2 + 3j
print("Conjugating:", z.conjugate())  # 2 - 3j


#4 Operations with complex numbers
# Addition
print("Addition:", z1 + z2)  # 4 + 6j

# Substraction
print("Substraction:", z1 - z2)  # -2 - 2j

# Multiplication
print("Multiplication:", z1 * z2)  # (1*3 - 2*4) + (1*4 + 2*3)j = -5 + 10j

# Division
print("Division:", z1 / z2)  # Complejo