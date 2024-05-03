#wrtie a simple menu driven phonebook application in python using dictionary where keys are names and values are phone numbers 
#Implement functionalities to add new contact,remove a contact,update a contact and lookup a contact's number

if __name__ == "__main__":
    phonebook = {}

    while True:
        print("\nTelephone System\n...............\n")
        print("1. Insert new contact")
        print("2. Delete a contact")
        print("3. Update a contact")
        print("4. Search for a person")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter the person's name: ")
            contact_number = input("Enter the contact number: ")
            if name not in phonebook:
                phonebook[name] = contact_number
                print("Successfully inserted into the phonebook.")
            else:
                print("Contact already exists.")
                print(f"Name: {name}\nContact number: {phonebook[name]}")

        elif choice == 2:
            name = input("Enter the person's name: ")
            if name in phonebook:
                del phonebook[name]
                print(f"Successfully deleted {name} from the phonebook.")
            else:
                print(f"Person '{name}' does not exist in the phonebook.")

        elif choice == 3:
            name = input("Enter the person's name: ")
            if name in phonebook:
                updated_contact_number = input("Enter the updated contact number: ")
                phonebook[name] = updated_contact_number
                print("Contact updated successfully.")
            else:
                print("The given user does not exist in the phonebook.")

        elif choice == 4:
            name = input("Enter the person's name: ")
            if name in phonebook:
                print(f"\n{name}'s Information:\nName: {name}\nContact Number: {phonebook[name]}")
            else:
                print("No such user found.")

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")