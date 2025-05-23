from tasks import (
    add_item,
    view_items,
    delete_item,
    view_total_items,
    set_budget,
    apply_discount
)

from menu import (
    show_menu,
    get_user_choice,
    handle_invalid_choice,
    handle_exit
)


def main():
    while True:
        show_menu()  # Display the menu options
        choice = get_user_choice()  # Get the user's choice

        if choice == '1':
            set_budget()  # Set the budget
        elif choice == '2':
            add_item()  # Add a new item
        elif choice == '3':
            view_items()  # View all items
        elif choice == '4':
            view_total_items()  # View total items
        elif choice == '5':
            delete_item()  # Delete an item
        elif choice == '6':
            apply_discount()  # Apply discount to an item
        elif choice == '7':
            handle_exit()  # Exit the application
            break  # Exit the loop and end the program
        else:
            handle_invalid_choice()  # Handle invalid choices


if __name__ == "__main__":
    main()  # Start the main function
