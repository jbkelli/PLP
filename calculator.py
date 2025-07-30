"""
Question to attempt
Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.
"""
print("Welcome to this simple python calculator. Please answer the prompts as asked.......")
print("..................")
#Asking for user input
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
operator = input("Choose an operator among(+, -, /, *)")
result = 0

#using if...elif...else to check the conditions to execute a particular operation
#Executing addition operator
if operator == "+":
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}")
    print(".........Program exited successfully.........")

#Executing subtraction operator
elif operator == "-":
    result = num1 - num2
    print(f"The difference between {num1} and {num2} is {result}")
    print(".............Program exited successfully......")

#Executing division operator
elif operator == "/":
    result = num1 / num2
    print(f"The quotient of {num1} and {num2} is {result}")
    print(".........Program exited successfully.........")

#Executing multiplication operator
elif operator == "*":
    result = num1 * num2
    print(f"The multiplication of {num1} and {num2} is {result}")
    print(".........Program exited successfully......")

#If all the elif blocks do not meet the conditions, this else block is executed
else:
    print("An error occured in the program!")