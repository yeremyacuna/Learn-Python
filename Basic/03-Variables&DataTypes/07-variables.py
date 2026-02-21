#### Variables and Data Types in Python

'''      ============= Variables ================     '''
x = 10
name = "Alice"
#1 Variable names must start with a letter or an underscore, and can contain letters, 
# digits, and underscores.

#2 Variable names are case-sensitive.
print(x, name)

#3 You can assign multiple variables at once.
a, b, c = 1, 2, 3
print(a, b, c)
name, age, university, pet = "Yeremy", 18, "UPC", "cat"
print("")
print(name, age, university, pet)
print("My name is", name, "and I'm", age, "years old. I study at", university, "and I have a", pet)
#4 You can also assign the same value to multiple variables.
x = y = z = 0
print(x, y, z, "\n")

#5 Variables can be reassigned to different values and types.
x = 10
print(x)
x = "Now I'm a string"
print(x)

#6 You can introduce values using the input() function, which always returns a string.
name = input("What's your name?" )
age = input("How old are you?" )
print(name)
print(age)

#7 You can specify the type of a variable using type hints, but it's not mandatory.
age: int = 18
print(age)
