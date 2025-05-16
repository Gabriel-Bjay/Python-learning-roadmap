from tasks import (
    add_tasks,
    view_tasks,
    delete_tasks,
    mark_completed
)  # imports all functions from tasks.py
from menu import (
    show_menu,
    get_user_choice,
    handle_invalid_choice,
    handle_exit
)  # imports all functions from menu.py


def main():
    tasks = []  # Initialize an empty list to store tasks
    while True:
        show_menu()  # Display the menu options
        choice = get_user_choice()  # Get the user's choice

        if choice == '1':
            tasks = add_tasks(tasks)  # Add a new task
        elif choice == '2':
            view_tasks(tasks)  # View all tasks
        elif choice == '3':
            mark_completed(tasks)  # Mark a task as completed
        elif choice == '4':
            delete_tasks(tasks)  # Delete a task
        elif choice == '5':
            handle_exit()  # Exit the application
            break  # Exit the loop and end the program
        else:
            handle_invalid_choice()  # Handle invalid choices


main()
