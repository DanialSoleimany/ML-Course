import json

try:
    path = "Projects/database.json"
    with open(path, 'r') as f:
        database = json.load(f)
except:
    database = {}
    with open(path, 'w') as f:
        json.dump(database, f, indent=4)

def add_contact(contact_name, contact_phone, contact_email):
    database[contact_name] = {
        "phone":contact_phone,
        "email":contact_email
    }

    with open(path, 'w') as f:
        json.dump(database, f, indent=4)

def remove_contact(contact_name):
    del database[contact_name]

    with open(path, 'w') as f:
        json.dump(database, f, indent=4)


def search_contact(contact_name):
    contact_info = database[contact_name]
    contact_phone = contact_info["phone"]
    contact_email = contact_info["email"]

    print(f"\nContact name is {contact_name}")
    print(f"Contact phone number is {contact_phone}")
    print(f"Contact email address is {contact_email}")
    

def show_menu():
    print("\nContact List")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Remove Contact")
    print("4. Edit Contact")
    print("5. Show All Contacts")
    print("6. Exit\n")

while True:
    show_menu()

    choice = int(input("What is your choice? "))

    if choice == 1:

        name = input("Enter a name: ")
        phone = input("Enter a phone number: ")
        email = input("Enter an email: ")

        add_contact(name, phone, email)

        print(f"{name} is successfully added to contact list\n")

    elif choice == 2:

        name = input("Enter a name: ")

        if name in database:
            search_contact(name)
        else:
            print(f"{name} is not exist")

    elif choice == 3:

        name = input("Enter a name: ")

        if name in database:
            remove_contact(name)
        else:
            print(f"{name} is not exist")

    elif choice == 6:
        break

    else:
        print("Wrong choice, try again!")