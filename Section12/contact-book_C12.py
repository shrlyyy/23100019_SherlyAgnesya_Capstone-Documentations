'''
Challenge 12: CLI Contact Book (CSV-Powered)

Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

Your program should:
1. Ask the user to choose one of the following options:
    - Add a new contact.
    - View all contacts.
    - Search for a contact by name.
    - Exit.
2. Store contacts in a file called 'contacts.csv' with columns:
    - Name.
    - Phone.
    - Email.
3. If the file doesn't exist, create it automatically.
4. Keep the interface clean and clear.

Example:
Add Contact
View All Contact
Search Contact
Exit

Bonus:
- Format the contact list in a table-like view.
- Allow partial match search.
- Prevent duplicate names from being added.
'''

import csv
import os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    # Check for duplicates.
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print("Contact name already exists.")
                return
            
    with open(FILENAME, 'a', newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
        print("Contact added.")

def view_contacts():
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows) < 1:
            print("No contacts found.")
            return
        
        print("\nYour contacts:\n")

        for row in rows[1:]:
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()

def search_contact():
    term = input("Enter the name to search: ").strip().lower()
    found = False

    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row["Name"].lower():
                print(f"{row["Name"]} | 📞 {row["Phone"]}")
                found = True

    if not found:
        print("No matching contact found.")

# Challenge: Bikin fitur delete.
def delete_contact():
        delete = input("Enter the name to delete: ").strip().lower()

        with open(FILENAME, 'r', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            rows = list(reader)

        new_data = [row for row in rows if row["Name"].lower() != delete]

        if len(new_data) == len(rows):
            print(f"Contact '{delete}' not found.")
        else:
            with open(FILENAME, 'w', newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(new_data)
            print(f"Contact '{delete}' successfully deleted.")



def main():
    while True:
        print("\n📚 Contact Book")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Thanks for using our software!")
            break
        else:
            print("Invalid choice of number.")

if __name__ == "__main__":
    main()
