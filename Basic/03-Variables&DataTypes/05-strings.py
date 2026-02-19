#### Variables and Data Types in Python

'''      ============= String type ================     '''
s1 = "Hello"
s2 = 'World'
s3 = """This is 
a multiline String
whith triple quotes."""
print(s1, s2)
print("\n" + s3)

#1 Strings can be concatenated using the + operator.
print("\n" + s1 + " " + s2) # Hello World

#2 Strings can be repeated using the * operator.
print(s1 * 3) # HelloHelloHello

#3 Strings are indexed (0-based).
print(s1[0]) # H
print(s1[-1]) # o
print(s1[-5]) # H

#4 Strings are immutable (you cannot change individual characters).
# s1[0] = "h"  # This would raise an error.

#5 String methods.
msg = " Hello python "

print("\nUpper:", msg.upper()) # HELLO PYTHON
print("Lower:", msg.lower()) # hello python
print("Title:", msg.title()) # Hello Python
print("Strip:", msg.strip()) # remove spaces
print("Replace:", msg.replace("python", "world"))
print("Find:", msg.find("python")) # index position
print(len(s1)) # 5

#6 String slicing.
print("\n" + s1[0:3]) # Hel
print(s1[3:5]) # lo

#7 Checking string content.
print("\nIs digit:", "123".isdigit()) # True
print("Is alpha:", "abc".isalpha()) # True
print("Is alnum:", "abc123".isalnum()) # True
print("Starts with:", "Python".startswith("Py")) # True
print("Ends with:", "Python".endswith("on")) # True

#7 Splitting and joining strings.
sentence = "I love Python"
words = sentence.split(" ")
print("Split:", words)

joined = "-".join(words)
print("Join:", joined)

#8 f-strings (formatted strings).
name = "Yeremy"
age = 20
print("\nMy name is " + name + f" and I am {age} years old.")


