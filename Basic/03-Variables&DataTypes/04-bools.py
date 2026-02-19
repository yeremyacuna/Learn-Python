#### Variables and Data Types in Python

'''      ============= Boolean type ================     '''
b1 = True
b2 = False
print(b1, b2)

#1 Booleans can be used in conditional statements.
if b1:
    print("b1 is True")

if not b2:
    print("b2 is False")

#2 Booleans are often the result of comparisons.
x = 10
y = 5

print("x > y:", x > y) # True
print("x < y:", x < y) # False
print("x == y:", x == y) # False
print("x != y:", x != y) # True

#3 Boolean operators: and, or, not
print("True and False:", True and False) # False
print("True or False:", True or False) # True
print("not True:", not True) # False

#4 Booleans can be converted using bool().
print(bool(1)) # True
print(bool(0)) # False
print(bool("")) # False (empty string)
print(bool("Hello")) # True (non-empty string)
print(bool([])) # False (empty list)

#5 Booleans behave like integers (True = 1, False = 0).
print(True + True) # 2
print(True * 5) # 5
print(False + 10) # 10