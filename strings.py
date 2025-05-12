message = "Hello, World!"
greeting = "Hello, User!"

email_msg = """Please check
your email for
further instructions."""

print(greeting [0:6]) #slicing

text1 = "Programming"
text2 = "Python"

#String concatenation
text3 = text1 + " " + text2
print(text3)

#String repetition
print ((text3 + "\n") * 2)

#String length
print (len(text3))

#string methods
print (text3.upper() + " This is  the uppercase version of the text") #convert to uppercase
print (text3.lower() + " Lowercase") #convert to lowercase
print (text3.title()) #convert to title case
print (text3.capitalize()) #convert to capitalized case
print (text3.strip()) #remove leading and trailing whitespace
print (text3.replace("Python", "Java")) #replace substring
print (text3.split(" ")) #split string into list

#substrings
print ("email" in email_msg) #check if substring exists