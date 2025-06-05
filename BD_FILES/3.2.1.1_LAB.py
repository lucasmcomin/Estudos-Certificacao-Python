import csv


class PhoneContact:
    
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        
        
        
        
class Phone:
    #responsible for reading data from the CSV file into the class property called contacts. The contacts property should contain a list of PhoneContact 
    # objects;
    def load_contacts_from_cvs(self):
        contacts = []
        with open('BD_FILES/contacts.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contacts.append(PhoneContact(row['Name'], row['Phone']))
        return contacts
        
    def search_contacts(self):
        # to the Phone class a method called search_contacts, which accepts any phrase entered by the user from the keyboard, 
        # and then based on it perform a search for all matching contacts (case insensitive). If there are no results, print the message: "No contacts found".
        contact_search = input("Search Contact: ").lower()
        contacts = self.load_contacts_from_cvs()
        flag = False
        for contact in contacts:
            if contact_search in contact.name.lower() or contact_search in contact.phone:
                print(contact.name + " (" + contact.phone + ")")
                flag = True
        
        if not flag:
            print("Contact not Found")
    


p = Phone()
p.search_contacts()

