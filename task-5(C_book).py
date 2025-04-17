import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from JSON file
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as f:
        return json.load(f)

# Save contacts to JSON file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Add new contact
def add_contact(contacts):
    print("\n📇 Add New Contact")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("✅ Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
        return
    print("\n📒 Contact List:")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")

# Search contact by name or phone
def search_contact(contacts):
    query = input("\n🔍 Enter name or phone to search: ").lower()
    results = [c for c in contacts if query in c["name"].lower() or query in c["phone"]]
    
    if results:
        print("\nSearch Results:")
        for c in results:
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}\n")
    else:
        print("❌ No matching contacts found.")

# Update contact
def update_contact(contacts):
    name = input("\n✏️ Enter the name of the contact to update: ").lower()
    for c in contacts:
        if c["name"].lower() == name:
            print("Leave blank to keep current value.")
            c["phone"] = input(f"New phone [{c['phone']}]: ") or c["phone"]
            c["email"] = input(f"New email [{c['email']}]: ") or c["email"]
            c["address"] = input(f"New address [{c['address']}]: ") or c["address"]
            print("✅ Contact updated successfully!")
            return
    print("❌ Contact not found.")

# Delete contact
def delete_contact(contacts):
    name = input("\n🗑️ Enter the name of the contact to delete: ").lower()
    for i, c in enumerate(contacts):
        if c["name"].lower() == name:
            del contacts[i]
            print("🗑️ Contact deleted.")
            return
    print("❌ Contact not found.")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n--- 📱 Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("📦 Contacts saved. Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
