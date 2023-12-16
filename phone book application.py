class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def edit_contact(self, old_name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name == old_name:
                self.contacts[i] = new_contact
                break

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

# Example usage:
if __name__ == "__main__":
    contact_manager = ContactManager()

    contact1 = Contact("John Doe", "123-456-7890", "john@gmail.com")
    contact2 = Contact("Jane Smith", "987-654-3210", "jane@gmail.com")

    contact_manager.add_contact(contact1)
    contact_manager.add_contact(contact2)

    contact_manager.display_contacts()

    # Edit contact
    new_contact = Contact("John Doe", "555-555-5555", "john@gmail.com")
    contact_manager.edit_contact("John Doe", new_contact)

    # Delete contact
    contact_manager.delete_contact("Jane Smith")

    contact_manager.display_contacts()