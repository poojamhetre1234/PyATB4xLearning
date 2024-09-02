### Task #3
# - Explain the difference between the = operator and the == operator in Python.
# - What does the ** operator do in Python, and how is it used?
# - What does the ^ operator do in Python, and in what context is it commonly used?

### - Explain the difference between the = operator and the == operator in Python.
#Ans->'=' Used to assign a value to a variable.
# It simply store the value on right-hand side into the variable on left-hand side.
#Ex: x = 5 here value 5 store in variable 'x'

# '==' Used to compare two values for equality.
#It returns True if the values on both sides are equal else False.
#Ex: x == 5 checks if the value of x is equal to 5.

# x = 5        # Assignment: x is now 5
# y = 10       # Assignment: y is now 10
#
# # Equality check:
# result = (x == y)  # Compares if x and y are equal; result will be False
# # because 5 is not equal to 10

### - What does the ** operator do in Python, and how is it used?
#Ans-> The ** operator in Python is used for exponentiation.
# The ** operator takes two operands:
# Base: The number you want to raise to a power (the number on the left).
# Exponent: The power to which the base is raised (the number on the right).
# base_number = float(input("Enter base number\n"))
# exponent = float(input("Enter exponent\n"))
# print(f"{base_number} raised to the power of {exponent} is ",f"{base_number ** exponent:.2f}")

# Ex: Exponentiation with negative exponent
# result = 5 ** -2
# print(result)  # Output: 0.04, because 5 raised to the power of -2 is 1/25 = 0.04

# # Ex:Exponentiation with floating-point numbers
# result = 9 ** 0.5
# print(result)  # Output: 3.0, because 9 raised to the power of 0.5 (square root) is 3.0

### - What does the ^ operator do in Python, and in what context is it commonly used?
#Ans->
# ^ operator or XOR (exclusive OR) operator is used to compare the corresponding bits
# of two integer numbers.
#It returns 1 if the bits are different i.e if one is 0 and one is 1
#It returns 0 if both the bits are same i.e both are 0 or both are 1
#Ex:
# num1 = int(input("Enter number1\t"))
# num2 = int(input("Enter number2\t"))
# print(f"The result is { num1 ^ num2}")