
print("Welcome to the Contact Management System!\nMenu:\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Quit")

contacts = {}  # Initialize an empty dictionary to store contacts

while True:
    selectItem = input("Which menu option would you like? (Add a new contact / Edit an existing contact / Delete a contact / Search for a contact / Display all contacts / Export contacts to a text file / Quit) ")

    if selectItem == "Add a new contact":
        newName = input("What is their name? ")
        newContact = input("What is the new phone number? ")
        newEmail = input("What is their email? ")

        contacts[newName] = [newContact, newEmail]
        print("Contact added:", contacts)
        # adds new contacts by name, email, and phone number
    elif selectItem == "Edit an existing contact":
        editName = input("Which contact would you like to edit? ")

        if editName in contacts:
            newContact = input("Enter the new phone number: ")
            newEmail = input("Enter the new email: ")
                # edits existing contacts
            contacts[editName] = [newContact, newEmail]  # Update the contact details
            print("Contact updated:", contacts)
        else:
            print("Contact not found.")

    elif selectItem.lower() == "quit":
        print("Exiting the menu.")
        break  # Exit the loop
    elif selectItem == "Delete a contact":
        deleteName = input("Which contact would you like to delete? ")

        if deleteName in contacts:
            del contacts[deleteName]  # Remove the contact
            print(f"Contact '{deleteName}' deleted.")
            print("Updated contacts:", contacts)
        else:
            print("Contact not found.")
    elif selectItem == "Search for a contact":
        searchPattern = input("Enter a name or pattern to search for: ")
        regex = re.compile(searchPattern, re.IGNORECASE)  # Compile the regex pattern

        found_contacts = {name: details for name, details in contacts.items() if regex.search(name)}
        
        if found_contacts:
            print("Found contacts:")
            for name, details in found_contacts.items():
                print(f"{name}: Phone - {details[0]}, Email - {details[1]}")
        else:
            print("No contacts found matching that pattern.")
    elif selectItem == "Display all contacts":
        print(contacts)
    elif selectItem == "Export contacts to a text file":
        with open("contacts.txt", "w") as file:
            file.write(contacts)
    elif selectItem == "Quit":
        break
        
    else:
        print("Invalid option. Please try again.")