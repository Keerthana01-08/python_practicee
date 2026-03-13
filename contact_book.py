contacts = {}

while True:
    print("\n1 Add Contact")
    print("2 View Contacts")
    print("3 Search Contact")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        contacts[name] = number

    elif choice == "2":
        for name, number in contacts.items():
            print(name, ":", number)

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print("Number:", contacts[name])
        else:
            print("Contact not found")

    elif choice == "4":
        break
