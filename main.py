def add_contact(name, contact):
    with open("contacts.txt", "a") as f:
        f.write(f"{name}:{contact}\n")


def view_contacts():
    try:
        with open("contacts.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("📭 No contacts found.\n")
            else:
                print("\n📒 Saved Contacts:")
                for i, line in enumerate(lines, 1):
                    try:
                        name, contact = line.strip().split(":")
                        print(f"{i}. 👤 Name: {name}, 📞 Contact: {contact}")
                    except ValueError:
                        continue  # skip malformed lines
                print()
    except FileNotFoundError:
        print("📂 contacts.txt file not found.\n")


while True:
    print("==== Contact Manager ====")
    print("1. ➕ Add Contact")
    print("2. 📖 View Contacts")
    print("3. 🚪 Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        name = input("Enter name: ")
        contact = input("Enter contact number: ")
        add_contact(name, contact)
        print("✅ Contact added successfully!\n")

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please try again.\n")
