#### Operators in Python

""" ============= Ways of Operating ================ """
a = 10; b = 20

#1 Using Parentheses
result1 = (a + b) * 2
print("Result using Parentheses:", result1)  # 60

#2 Using Variables
temp = a + b
result2 = temp * 2
print("Result using Variables:", result2)  # 60

#3 Using Functions
def operate(x, y):
    return (x + y) * 2
result3 = operate(a, b)
print("Result using Functions:", result3)  # 60

#4 Using Lambda Functions
operate_lambda = lambda x, y: (x + y) * 2
result4 = operate_lambda(a, b)
print("Result using Lambda Functions:", result4)  # 60

#5 Using strings 
expression = "(a + b) * 2"
result5 = eval(expression)
print("Result using Strings:", result5)  # 60

#6 Operations with strings
print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5))

#7 Repetition of strings
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

#8 Operations with strings and comparison
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

#9 Logical operations with strings and numbers https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))