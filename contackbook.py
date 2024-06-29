class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_new_contact(self, name, phone_number, email, address):
        if self.validate_email(email):
            self.contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
            print(f"Yay! I've added {name} to your contact book")
        else:
            print("Invalid email address. Please try again")

    def view_all_contacts(self):
        if not self.contacts:
            print("Your contact book is empty")
        else:
            print("Here are all your contacts:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone Number: {details['phone_number']}")

    def search_for_contact(self, query):
        found = False
        for name, details in self.contacts.items():
            if query in name or query in details['phone_number']:
                print(f"Name: {name}, Phone Number: {details['phone_number']}, Email: {details['email']}, Address: {details['address']}")
                found = True
        if not found:
            print("Sorry, I couldn't find that contact")

    def update_contact_info(self, name, phone_number=None, email=None, address=None):
        if name in self.contacts:
            if phone_number:
                self.contacts[name]['phone_number'] = phone_number
            if email:
                if self.validate_email(email):
                    self.contacts[name]['email'] = email
                else:
                    print("Invalid email address. Please try again")
            if address:
                self.contacts[name]['address'] = address
            print(f"I've updated {name}'s info for you")
        else:
            print("Sorry, I couldn't find that contact")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"I've removed {name} from your contact book")
        else:
            print("Sorry, I couldn't find that contact")

    def validate_email(self, email):
        if "@" in email and "." in email:
            return True
        else:
            return False


def main():
    my_contact_book = ContactBook()

    while True:
        print("\nWelcome to Your Contact Book")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Update a contact's info")
        print("5. Delete a contact")
        print("6. Quit")

        choice = input("What would you like to do ")

        if choice == '1':
            name = input("Enter the contact's name: ")
            phone_number = input("Enter their phone number: ")
            email = input("Enter their email: ")
            address = input("Enter their address: ")
            my_contact_book.add_new_contact(name, phone_number, email, address)
        elif choice == '2':
            my_contact_book.view_all_contacts()
        elif choice == '3':
            search = input("Enter a name or phone number to search for: ")
            my_contact_book.search_for_contact(search)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone_number = input("Enter their new phone number (optional): ")
            email = input("Enter their new email (optional): ")
            address = input("Enter their new address (optional): ")
            my_contact_book.update_contact_info(name, phone_number if phone_number else None, email if email else None, address if address else None)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            my_contact_book.delete_contact(name)
        elif choice == '6':
            break
        else:
            print("Sorry, that's not a valid option. Try again")


if __name__ == "__main__":
    main()