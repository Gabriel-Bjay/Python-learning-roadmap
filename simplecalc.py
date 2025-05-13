num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Select the operation (+, -, *, /): ")
# Perform the operation
if operation == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is : {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result of {num1} x {num2} is : {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is : {result}")
    else:
        print("Error: Division by zero is not allowed.")