# Initialize an empty dictionary to store contacts
contacts = dict(
    Allan=dict(Contact="0711477823"),
    Bob=dict(Contact="0700477823"),
    Charlie=dict(Contact="0799077823"),
    David=dict(Contact="0711887823")
)


def is_valid_phone_number(number):
    return number.isdigit() and len(number) == 10


def add_contact(contacts):
    """
    Function to add a new contact to the phonebook.
    Prompts the user for the contact's name and phone number.
    Checks if the contact already exists in the phonebook.
    """
    name = input("Enter the contact's name: ").capitalize().strip()
    phone_number = input("Enter the contact's phone number: ")
    # Check if the contact already exists
    if name in contacts:
        print(f"Contact {name} already exists with number {contacts[name]}.")
    else:
        # Add the new contact to the phonebook
        contacts[name] = dict(Contact=phone_number)
        print(f"Contact {name} added with number {phone_number}.")
    return contacts


def search_contact(contacts):
    name = input("Enter the contact's name to search: ").strip()
    key = find_contact_key(name, contacts)
    if key:
        print(f"{key}: {contacts[key]['Contact']}")
    else:
        print("Contact not found.")


def delete_contact(contacts):
    """
    Function to delete a contact from the phonebook.
    Prompts the user for the contact's name to be deleted.
    Checks if the contact exists in the phonebook.
    """
    name = input("Enter the contact's name to delete: ").capitalize().strip()
    # Check if the contact exists
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} does not exist.")
    return contacts


def view_contacts(contacts):
    if contacts:
        print("Phonebook Contacts:")
        for name, details in contacts.items():
            print(f"{name}: {details['Contact']}")
    else:
        print("No contacts found.")


view_contacts(contacts)


def find_contact_key(name, contacts):
    """
    Helper to find the actual dictionary key (original casing)
    for a contact by doing case-insensitive matching.
    Returns the key or None if not found.
    """
    lower_name = name.lower()
    for key in contacts:
        if key.lower() == lower_name:
            return key
    return None
