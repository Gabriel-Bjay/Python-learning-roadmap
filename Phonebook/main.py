"""
    Building a simple phonebook dictionary
    that allows users to look up contacts, add, delete, and update contacts.
"""
from tasks import (
    add_contact,
    delete_contact,
    view_contacts,
    contacts,
    search_contact
    )


def main():
    print("Hello! Welcome to the Phonebook App.")
    print("You can add, delete, and view contacts.")
    print("Options:")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Exit")

    # User input loop
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            delete_contact(contacts)
        elif choice == '3':
            view_contacts(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            print("Exiting the Phonebook App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
