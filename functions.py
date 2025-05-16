# function that adds 3 numbers
name = input("Enter your name: ").title()
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
def add_numbers(a, b, c):
    return a + b + c
output = add_numbers(a, b, c)
# Print the result
print(f"Hello {name}, the sum of {a}, {b}, and {c} is: {output}")

#function that checks if a number is even
number = int(input("Enter a number to check if it's even: "))
def is_even(number):
    return number % 2 == 0
# Check if the number is even
if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


#Function to concatenate two strings
string1 = input("Enter your first name: ").title()
string2 = input("Enter your last name: ").title()

def full_name(string1, string2):
    return string1 + " " + string2
# Call the function and print the result
result = full_name(string1, string2)
print(f"Hello {result}, welcome to the program!")


#lambda function
full_name = lambda fname, lname: fname + " " + lname
# Get user input
fname = input("Enter your first name: ").title()
lname = input("Enter your last name: ").title()
# Call the lambda function and print the result
result = full_name(fname, lname)
print(f"Hello {result}, welcome to the program that uses lambda function!")