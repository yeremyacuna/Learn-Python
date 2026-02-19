#### Variables and Data Types in Python

'''      ============= How to identify it? ================     '''
print(type("hola")) # String
print(type(42)) # Integer
print(type(3.14)) # Float
print(type(2j+2j+0)) # Complex number
print(type(False)) # Boolean
print(type(None)) # NoneType
print(type(b"hello")) # Bytes

print(type([1, 2, 3])) # List
print(type((1, 2, 3))) # Tuple
print(type({1, 2, 3})) # Set
print(type({"name": "Yeremy", "age": 30})) # Dictionary
print(type(frozenset([1, 2, 3]))) # Frozenset
print(type(bytearray(5))) # Bytearray
print(type(memoryview(b"hello"))) # Memoryview
print(type(range(5))) # Range

print(type(print)) # Built-in function
print(type(int)) # Type

# Note: The type() function is used to determine the data type of a value or variable in Python.

#1 Change the value of a variable and check its type again.
my_var = "Hello"
print("\n"+ str(type(my_var))) # str
my_var = 123
print(type(my_var)) # int

#2 Convert a variable from one type to another and check the new type.
age = 18
print("\n"+ str(type(age))) # int
print(age)

age = str(age)
print(type(age)) # int -> str

age_float =float(age) # int -> float
print(age_float)

#3 Reassign a variable to a different type and check its type.
name = "Yeremy"
print("\n"+ name)

name = 12345
print(name)

print(type(name)) # str -> int