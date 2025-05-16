def show_menu():
    print("Welcome to the To-Do List Application!")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")


def get_user_choice():
    return input("Please enter your choice (1-5): ")


def handle_invalid_choice():
    print("Invalid choice. Please try again.")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")


def handle_exit():
    print("Thank you for using the To-Do List Application. Goodbye!")
