# Creating the menu to welcome the user to the Budget Tracker Application


def show_menu():
    print(
        "Welcome to the Budget Tracker Application!"
        "\nThis application helps you manage your budget "
        "and track your expenses."
    )
    print("1. Set budget")
    print("2. Add a new item")
    print("3. View items")
    print("4. View total items")
    print("5. Delete an item")
    print("6. Apply Discount")
    print("7. Exit")


# Function to get user input
def get_user_choice():
    return input("Please enter your choice (1-7): ")


# Function to handle invalid choice
def handle_invalid_choice():
    print("Invalid choice. Please try again.")
    print("1. Set budget")
    print("2. Add a new item")
    print("3. View items")
    print("4. View total items")
    print("5. Delete an item")
    print("6. Apply Discount")
    print("7. Exit")


# Function to handle exit
def handle_exit():
    print("Thank you for using the Budget Tracker Application. Goodbye!")
