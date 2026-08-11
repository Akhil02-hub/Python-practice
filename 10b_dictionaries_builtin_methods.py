"""
Dictionary Practice - Built-in Methods Version
Same 15 problems as 10_dictionaries.py, solved using Python's
built-in dictionary methods (.items(), max(key=...)) instead of
manual loops - shows both approaches to the same problems.
"""


# Q1. Create a Dictionary
def create_dictionary():
    student = {}

    student["name"] = input("Enter name: ")
    student["age"] = int(input("Enter age: "))
    student["course"] = input("Enter course: ")

    print(student)


# Q2. Display Dictionary
def display_dictionary():
    student = {
        "name": "Akhil",
        "age": 18,
        "course": "CSE"
    }

    for key, value in student.items():
        print(key, ":", value)


# Q3. Search a Key
def search_key():
    student = {
        "name": "Akhil",
        "age": 18,
        "course": "CSE"
    }

    key = input("Enter key: ")

    if key in student:
        print(student[key])
    else:
        print("Key not found")


# Q4. Update a Value
def update_value():
    student = {
        "name": "Akhil",
        "age": 18,
        "course": "CSE"
    }

    key = input("Enter key to update: ")

    if key in student:
        value = input("Enter new value: ")
        student[key] = value
        print(student)
    else:
        print("Key not found")


# Q5. Delete a Key
def delete_key():
    student = {
        "name": "Akhil",
        "age": 18,
        "course": "CSE"
    }

    key = input("Enter key to delete: ")

    if key in student:
        del student[key]
        print(student)
    else:
        print("Key not found")


# Q6. Character Frequency
def character_frequency():
    text = input("Enter a string: ")

    freq = {}

    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    print(freq)


# Q7. Word Frequency
def word_frequency():
    sentence = input("Enter a sentence: ")

    words = sentence.split()

    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    print(freq)


# Q8. Merge Dictionaries
def merge_dictionary():
    d1 = {
        "A": 10,
        "B": 20
    }

    d2 = {
        "C": 30,
        "D": 40
    }

    d1.update(d2)

    print(d1)


# Q9. Highest Value (using max with key=)
def highest_value():
    marks = {
        "A": 90,
        "B": 80,
        "C": 95
    }

    highest = max(marks, key=marks.get)

    print(highest)


# Q10. Reverse Dictionary
def reverse_dictionary():
    d = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    reverse = {}

    for key, value in d.items():
        reverse[value] = key

    print(reverse)


# Q11. Student Record System
def student_record():
    students = {}

    while True:
        print("\n1.Add")
        print("2.Search")
        print("3.View")
        print("4.Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            roll = input("Enter roll: ")
            name = input("Enter name: ")

            students[roll] = name

        elif choice == "2":
            roll = input("Enter roll: ")

            if roll in students:
                print(students[roll])
            else:
                print("Student not found")

        elif choice == "3":
            print(students)

        elif choice == "4":
            break


# Q12. Inventory System
def inventory():
    items = {}

    while True:
        print("\n1.Add")
        print("2.Update")
        print("3.Delete")
        print("4.Display")
        print("5.Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            product = input("Product: ")
            quantity = int(input("Quantity: "))

            items[product] = quantity

        elif choice == "2":
            product = input("Product: ")

            if product in items:
                items[product] = int(input("New quantity: "))

        elif choice == "3":
            product = input("Product: ")

            if product in items:
                del items[product]

        elif choice == "4":
            print(items)

        elif choice == "5":
            break


# Q13. Voting System (winner found via max with key=)
def voting():
    votes = {}

    n = int(input("Number of votes: "))

    for i in range(n):
        candidate = input("Vote: ")

        if candidate in votes:
            votes[candidate] += 1
        else:
            votes[candidate] = 1

    winner = max(votes, key=votes.get)

    print(votes)
    print("Winner:", winner)


# Q14. Phone Book
def phone_book():
    contacts = {}

    while True:
        print("\n1.Add")
        print("2.Search")
        print("3.Delete")
        print("4.View")
        print("5.Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")

            contacts[name] = phone

        elif choice == "2":
            name = input("Name: ")

            if name in contacts:
                print(contacts[name])

        elif choice == "3":
            name = input("Name: ")

            if name in contacts:
                del contacts[name]

        elif choice == "4":
            print(contacts)

        elif choice == "5":
            break


# Q15. Dictionary CRUD
def dictionary_crud():
    data = {}

    while True:
        print("\n1.Add")
        print("2.Update")
        print("3.Delete")
        print("4.Search")
        print("5.Display")
        print("6.Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            key = input("Key: ")
            value = input("Value: ")

            data[key] = value

        elif choice == "2":
            key = input("Key: ")

            if key in data:
                data[key] = input("New Value: ")

        elif choice == "3":
            key = input("Key: ")

            if key in data:
                del data[key]

        elif choice == "4":
            key = input("Key: ")

            if key in data:
                print(data[key])
            else:
                print("Key not found")

        elif choice == "5":
            print(data)

        elif choice == "6":
            break


if __name__ == "__main__":
    print("1. Create Dictionary")
    print("2. Display Dictionary")
    print("3. Search Key")
    print("4. Update Value")
    print("5. Delete Key")
    print("6. Character Frequency")
    print("7. Word Frequency")
    print("8. Merge Dictionary")
    print("9. Highest Value")
    print("10. Reverse Dictionary")
    print("11. Student Record")
    print("12. Inventory")
    print("13. Voting")
    print("14. Phone Book")
    print("15. Full Dictionary CRUD Menu")

    choice = input("Choose: ")

    if choice == "1":
        create_dictionary()
    elif choice == "2":
        display_dictionary()
    elif choice == "3":
        search_key()
    elif choice == "4":
        update_value()
    elif choice == "5":
        delete_key()
    elif choice == "6":
        character_frequency()
    elif choice == "7":
        word_frequency()
    elif choice == "8":
        merge_dictionary()
    elif choice == "9":
        highest_value()
    elif choice == "10":
        reverse_dictionary()
    elif choice == "11":
        student_record()
    elif choice == "12":
        inventory()
    elif choice == "13":
        voting()
    elif choice == "14":
        phone_book()
    elif choice == "15":
        dictionary_crud()
    else:
        print("Invalid choice")
