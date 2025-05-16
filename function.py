name = input("Enter your name: ")
# Ask for two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# Function to greet the user

def greet(name):
    print(f"Hello, {name}!")
greet(name)
#Function to add 2 numbers
def add(a, b):
    return a + b
print("Welcome to the addition program!")
# Call the add function and print the result
result = add(a, b)
print(f"Hello {name}, the sum of {a} and {b} is {result}.")

def multiply(a, b):
    return a * b
print("Welcome to the multiplication program!")
# # Call the multiply function and print the result
result = multiply(a, b)
print(f"Hello {name}, the product of {a} and {b} is {result}.")

#Function to return square of a number
def square(a):
    return a ** 2
print("Welcome to the square program!")
# Call the square function and print the result
result = square(a)
print(f"Hello {name}, the square of {a} is {result}.")

#lambda function that returns the square of a number
square = lambda a: (a ** 2)
# Call the lambda function and print the result
result = square(a)