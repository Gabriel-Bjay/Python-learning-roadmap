#Ask user for 2 numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#perform operations to add and find difference
sum = num1 + num2
difference = num1 - num2
print(f"The sum of {num1} + {num2} is: {sum} whereas the difference of {num1} - {num2} is: {difference}")

##Reassigning the values of sum
sum += 10
print(f"The new value of sum after adding 10 is: {sum}")

#Performing multiplication and division
# Check for division by zero
if (num1 or num2) == 0:
    print("Error: Division by zero is not allowed.")
elif (num2 and num1 != 0):
    product = num1 * num2
    quotient = num1 / num2
    print(f"The product of {num1} * {num2} is: {product} whereas the quotient of {num1} / {num2} is: {quotient}")
else:
    print("Error: Invalid operation.")
#Check if the 2 numbers are equal
if num1 == num2:
    print(f"The numbers {num1} and {num2} are equal.")
else:
    print(f"The numbers {num1} and {num2} are not equal.")