"""
Dictionary Practice
Topics: create, display, search, update, delete, character/word
frequency, merge, highest value, reverse dict, student record system,
inventory system, voting system, phone book, full CRUD project
"""


# 1. Create a Dictionary
def create_dict():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    print(student)


# 2. Display Dictionary
def display_dict():
    student = {"name": "Akhil", "age": 18, "course": "CSE"}

    for key in student:
        print(key, ":", student[key])


# 3. Search a Key
def search_key():
    student = {"name": "Akhil", "age": 18, "course": "CSE"}

    key = input("Enter key: ")

    if key in student:
        print(student[key])
    else:
        print("Key not found")


# 4. Update a Value
def update_value():
    student = {"name": "Akhil", "age": 18, "course": "CSE"}

    key = input("Enter key to update: ")
    value = input("Enter new value: ")

    if key in student:
        student[key] = value
        print(student)
    else:
        print("Key not found")


# 5. Delete a Key
def delete_key():
    student = {"name": "Akhil", "age": 18, "course": "CSE"}

    key = input("Enter key to delete: ")

    if key in student:
        del student[key]
        print(student)
    else:
        print("Key not found")


# 6. Count Frequency of Characters
def char_frequency():
    s = input("Enter a string: ")
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for key in freq:
        print(key, ":", freq[key])


# 7. Word Frequency
def word_frequency():
    s = input("Enter a sentence: ")
    words = s.split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    for key in freq:
        print(key, ":", freq[key])


# 8. Merge Dictionaries
def merge_dicts():
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}

    d1.update(d2)
    print(d1)


# 9. Find Highest Value
def highest_value():
    marks = {"A": 90, "B": 80, "C": 95}

    max_key = ""
    max_value = -1

    for key in marks:
        if marks[key] > max_value:
            max_value = marks[key]
            max_key = key

    print(max_key)


# 10. Reverse Dictionary
def reverse_dict():
    d = {"A": 1, "B": 2, "C": 3}
    rev = {}

    for key in d:
        rev[d[key]] = key

    print(rev)


# 11. Student Record System
def student_system():
    students = {}

    while True:
        print("\n1. Add")
        print("2. Search")
        print("3. View")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            roll = input("Enter roll number: ")
            name = input("Enter name: ")
            course = input("Enter course: ")

            students[roll] = {"name": name, "course": course}
            print("Student added")

        elif choice == "2":
            roll = input("Enter roll number: ")
            if roll in students:
                print(students[roll])
            else:
                print("Student not found")

        elif choice == "3":
            print(students)

        elif choice == "4":
            break

        else:
            print("Invalid choice")


# 12. Inventory System
def inventory_system():
    inventory = {}

    while True:
        print("\n1. Add Product")
        print("2. Update Quantity")
        print("3. Delete Product")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            product = input("Enter product name: ")
            qty = int(input("Enter quantity: "))
            inventory[product] = qty

        elif choice == "2":
            product = input("Enter product name: ")
            qty = int(input("Enter new quantity: "))
            if product in inventory:
                inventory[product] = qty
            else:
                print("Product not found")

        elif choice == "3":
            product = input("Enter product name: ")
            if product in inventory:
                del inventory[product]
            else:
                print("Product not found")

        elif choice == "4":
            print(inventory)

        elif choice == "5":
            break

        else:
            print("Invalid choice")


# 13. Voting System
def voting_system():
    votes = {}

    n = int(input("Enter number of votes: "))

    for i in range(n):
        candidate = input("Enter candidate name: ")

        if candidate in votes:
            votes[candidate] += 1
        else:
            votes[candidate] = 1

    winner = ""
    max_votes = 0

    for key in votes:
        if votes[key] > max_votes:
            max_votes = votes[key]
            winner = key

    print("Votes:", votes)
    print("Winner:", winner)


# 14. Phone Book
def phone_book():
    contacts = {}

    while True:
        print("\n1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            contacts[name] = phone

        elif choice == "2":
            name = input("Enter name: ")
            if name in contacts:
                print(contacts[name])
            else:
                print("Contact not found")

        elif choice == "3":
            name = input("Enter name: ")
            if name in contacts:
                del contacts[name]
            else:
                print("Contact not found")

        elif choice == "4":
            print(contacts)

        elif choice == "5":
            break

        else:
            print("Invalid choice")


# 15. Dictionary CRUD Project
def dict_crud():
    data = {}

    while True:
        print("\n1. Add")
        print("2. Update")
        print("3. Delete")
        print("4. Search")
        print("5. Display")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            key = input("Enter key: ")
            value = input("Enter value: ")
            data[key] = value

        elif choice == "2":
            key = input("Enter key: ")
            value = input("Enter new value: ")
            if key in data:
                data[key] = value
            else:
                print("Key not found")

        elif choice == "3":
            key = input("Enter key: ")
            if key in data:
                del data[key]
            else:
                print("Key not found")

        # Fixed: original had "choice" split across a line break
        # ("elif c" / "hoice == ...") which is a SyntaxError.
        elif choice == "4":
            key = input("Enter key: ")
            if key in data:
                print(data[key])
            else:
                print("Key not found")

        elif choice == "5":
            print(data)

        elif choice == "6":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    dict_crud()
    # create_dict()
    # display_dict()
    # search_key()
    # update_value()
    # delete_key()
    # char_frequency()
    # word_frequency()
    # merge_dicts()
    # highest_value()
    # reverse_dict()
    # student_system()
    # inventory_system()
    # voting_system()
    # phone_book()
