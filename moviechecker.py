#Ask for age
age = int(input("Enter age to verify eligibility: "))
student_id = input("Do you have a student ID? (yes/no): ").strip().lower()
#Ask for time of movie
time = input("Enter time of movie in 24hr-format: ")

#Check for eligibility
if age >= 18:
    print("You are eligible to book the ticket.")
elif age <= 18 and student_id == "yes" and time < "1800":
    print("You are eligible to book the ticket with a student ID.")
elif age <= 18 and student_id == "yes" and time > "1800":
    print("You cannot book the ticket right now! Come back tomorrow")
else:
    print("Sorry, you are not eligible to book the ticket.")