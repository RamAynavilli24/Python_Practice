class Contact:
    phone_directory = []

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        Contact.phone_directory.append(self)

    def show_contact(self):
        return f"Name: {self.name}, Phone Number: {self.phone_number}"

    @classmethod
    def show_all_contacts(cls):
        if len(cls.phone_directory) == 0:
            print("Your contacts list is empty")
        else:
            for contact in cls.phone_directory:
                print(contact.show_contact())

    @classmethod
    def search_contact(cls, search_name):
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                print("Results for contact you entered..........")
                return f"Name: {contact.name}, Phone Number: {contact.phone_number}"
        return f"No Contact found in your contacts list"

    @classmethod
    def delete_contact(cls, contact_id):
        for contact in cls.phone_directory:
            if contact.name.lower() == contact_id.lower():
                cls.phone_directory.remove(contact_id)
                return f"Contact {contact_id} deleted"
        return f"No Contact found in your contacts list"

    @staticmethod
    def validate_phone_number(contact_number):
        if len(contact_number) >= 8 and contact_number.isdigit():
            return True
        else:
            return False
n_contacts = int(input("How many contacts do you want?"))

for i in range(n_contacts):
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    if Contact.validate_phone_number(phone_number):
        Contact(name, phone_number)

c1 = Contact("Naresh",908763543)
c2 = Contact("Ruth",9876547639)



#print(Contact.phone_directory)

Contact.show_all_contacts()

print(Contact.search_contact(input("Enter your name: ")))
print(Contact.delete_contact(input("Enter your contact ID: ")))
