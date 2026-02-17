"""
File: comments.py
Description: Demonstrates different types of comments and docstrings in Python.
Author: Yeremy
"""

# ----------------------------------------
# 1. Single-line comment
# ----------------------------------------

# This is a standard single-line comment
print("Python comments example")


# ----------------------------------------
# 2. Inline comment
# ----------------------------------------

age = 19  # Storing the user's age


# ----------------------------------------
# 3. Section separator comment
# (Used for visual organization only)
# ----------------------------------------

# ====== USER INFORMATION SECTION ======


# ----------------------------------------
# 4. Commenting out code
# ----------------------------------------

# print("This line is temporarily disabled")


# ----------------------------------------
# 5. Function with docstring
# Docstrings are used for documentation
# ----------------------------------------

def greet(name):
    """
    Prints a greeting message using the provided name.

    Parameters:
        name (str): The name of the user.
    """
    print("Hello,", name)


greet("Yeremy")
