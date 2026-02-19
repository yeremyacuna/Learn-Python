#### Variables and Data Types in Python

'''      ============= Data Structures ================     '''
## ========== 1 Lists: ordered, mutable collections of items. ==========
    #- Can contain mixed types.
    #- Defined with square brackets [].
    #- Duplicates allowed.
    #- It can change its size and content.
my_list = [1, "hello", 3.14, True] 
numbers = [1,2,3,4,5,6,7,8,9,10]
print(my_list)
   
    #1.1- Accessing list elements by index
print(my_list[0]) # 1
print(my_list[1]) # "hello"
print(numbers[-1]) # 10

    #1.2- Modifying list elements
my_list[0] = 42
print(my_list) # [42, "hello", 3.14, True]

    #1.3- List methods
numbers.append(99) # add to end
print(numbers) # [1,2,3,4,5,6,7,8,9,10,99]

numbers.insert(5, 0) # add at index 5 element 0
print(numbers) # [0,1,2,3,4,5,6,7,8,9,10,99]

numbers.remove(3) # remove first occurrence of 3
print(numbers) # [0,1,2,4,5,6,7,8,9,10,99]

numbers.pop() # remove last element
print(numbers) # [0,1,2,4,5,6,7,8,9,10]

numbers.pop(0) # remove element at index 0
print(numbers) # [1,2,4,5,6,7,8,9,10]

print(len(numbers)+1) # 10 (after removing 1 element because the list started with 0 to 10)



## ========== 2 Tuples: ordered, immutable collections of items. ==========
    #- Can contain mixed types.
    #- Defined with parentheses ().
    #- Duplicates allowed.
    #- Cannot change its size or content after creation.
my_tuple = (1, "hello", 3.14, False, 1+3j, "hello" , 'GitHub')
print(my_tuple)
   
    #2.1- Accessing tuple elements by index
print(my_tuple[0]) # 1
print(my_tuple[1]) # "hello"
print(my_tuple[-1]) # 'GitHub' ####my_tuple[1] = 3 # This will raise an error because tuples are immutable.
   
    #2.2- Tuple methods
print(len(my_tuple)) # 6
print(my_tuple.count("hello")) # 2 (number of occurrences of "hello")
print(my_tuple.index("GitHub")) # 6 (index of first occurrence of "GitHub")

## ========== 3 Sets: unordered, mutable collections of unique items. ==========
    #- Can contain mixed types.
    #- Defined with curly braces {}.
    #- No duplicates allowed.
    #- Cannot be indexed or sliced.
my_set = {1, "hello", 3.14, False, 1+3j, "hello" , 'GitHub', 1, 1, 1}
my_set_correct = {1, "hello", 3.14, False, 1+3j, 'GitHub'}
print(my_set) #  (duplicates removed and order is not guaranteed)
print(my_set_correct, "\n")
    
     #3.1- Set methods
my_set_correct.add("YEREMY") # Add an element to a random index.
print(my_set_correct)
my_set_correct.remove(3.14) # Remove an element
print(my_set_correct)

## ========== 4 Dictionaries: unordered, mutable collections of key-value pairs. ==========
    #- Keys must be unique and immutable (strings, numbers, tuples).
    #- Values can be of any type and can be duplicated.
    #- Defined with curly braces {} with key-value pairs separated by colons.
my_dict ={
    "name": "Yeremy",
    "age": 18,
    "university": "UPC",
    "pet": "cat",
    "hobbies": ["programming", "gaming", "traveling"],
    "is_student": True
}
print("\n"+str(my_dict), "\n\n")

    #4.1- Accessing dictionary values by key
print(my_dict["name"]) 
print(my_dict["age"]) 
print(my_dict["hobbies"], "\n")

    #4.2- Modifying dictionary values
my_dict["age"] = 19
print(my_dict, "\n\t")

    #4.3- Adding new key-value pairs
my_dict["favorite_color"] = "blue"
my_dict["favorite_singer"] = "Mora", "Cris MJ", "Rauw Alejandro"
print(my_dict)
my_dict["hobbies"].append("cooking") # Modifying a list inside the dictionary
print(my_dict, "\n\n")

    #4.4- Dictionary methods
print(my_dict.keys()) # dict_keys(['name', 'age', 'university', 'pet', 'hobbies', 'is_student', 'favorite_color', 'favorite_singer'])
print(my_dict.values()) # dict_values(['Yeremy', 19, 'UPC', 'cat', ['programming', 'gaming', 'traveling', 'cooking'], True, 'blue', ('Mora', 'Cris MJ', 'Rauw Alejandro')])
print(my_dict.items()) # dict_items([('name', 'Yeremy'), ('age', 19), ('university', 'UPC'), ('pet', 'cat'), ('hobbies', ['programming', 'gaming', 'traveling', 'cooking']), ('is_student', True), ('favorite_color', 'blue'), ('favorite_singer', ('Mora', 'Cris MJ', 'Rauw Alejandro'))])
print(len(my_dict)) # 8 (number of key-value pairs)

