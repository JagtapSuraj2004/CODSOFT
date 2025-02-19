import json
import os
import re


CONTACTS_FILE = 'contacts.json'


def load_contacts():
    """Load contacts from the JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    """Add a new contact with phone number validation."""
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone number: ").strip()


    if len(phone) > 10:
        print("Phone number should not exceed 10 digits.")
        return


    if not re.match(r'^\d+$', phone):
        print("Phone number should contain only digits.")
        return

    email = input("Enter contact email: ").strip()
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact '{name}' added.")


def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}\n")


def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")


def search_contact(contacts):
    """Search for a contact."""
    name = input("Enter contact name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
    else:
        print("Contact not found.")


def main():
    contacts = load_contacts()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()