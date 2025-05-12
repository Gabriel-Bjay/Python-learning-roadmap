name = input("Hello! What is your name? ")
age = input("How old are you? ")
occupation = input("What is your occupation? ")
# Display the user input
print (f"\nHello {name}, aged {age}, who works as a {occupation}. How are you feeling today?")

#Reversing the order of the string
reversed_name = name[::-1]
print (f"Your name in reverse is: {reversed_name}")

#string reversal using loop
reversed_name_loop = ""
for char in name:
    reversed_name_loop = char + reversed_name_loop
print (f"Your name in reverse using loop is: {reversed_name_loop}")