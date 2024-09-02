### Task #5
#- Create a program that takes two numbers as input and prints whether
# the first number is greater than, less than, or equal to the second number.
num1=float(input("Enter num1:"))
num2=float(input("Enter num2:"))
if (num1>num2):
    print(f"The {num1} is greater than {num2}")
elif (num1<num2):
    print(f"The {num1} is less than {num2}")
elif (num1==num2):
    print(f"{num1} and {num2} are equal")

