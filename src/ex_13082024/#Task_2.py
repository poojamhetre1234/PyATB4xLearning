# Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))

print(f"The maximum number between {num1} & {num2} is", max(num1,num2))
print(f"The power of {num1}**{num2}={num1**num2}")
print(f"The Sum of {num1} + {num2} = {num1+num2}")
print(f"The Sub of {num1} - {num2} = {num1-num2}")
print(f"The Div of {num1} / {num2} = {num1/num2}")
print(f"The Multiplication of {num1} * {num2} = {num1*num2} ")
