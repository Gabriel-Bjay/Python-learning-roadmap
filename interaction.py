name = input ("What is your name? ")
age = input ("What is your age? ")
fav_number = input ("What is your favorite number? ")
#Display the user input
print ("\nYou have provided the following information:")
print (f"Name: {name}")
print (f"Age: {age}")
print (f"Favorite Number: {fav_number}")

#Type casting favorite number to float
fav_number = float(fav_number)
#Display the type of favorite number
print (f"Type of Favorite Number after casting: {type(fav_number)}")
#Display favorite number in float form
print (f"Favorite Number in float form: {fav_number}")