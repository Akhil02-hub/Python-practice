"""
File Handling Practice
Topics: write, read, append, count characters/lines/words, copy,
search/replace word, longest line, remove duplicates, reverse,
merge files, student record system, mini notes app
"""


# 1. Write to a File
def write_file():
    filename = input("Enter file name: ")
    text = input("Enter text to write: ")

    with open(filename, "w") as file:
        file.write(text)

    print("Data written successfully")


# 2. Read a File
def read_file():
    filename = input("Enter file name: ")

    with open(filename, "r") as file:
        print(file.read())


# 3. Append to a File
def append_file():
    filename = input("Enter file name: ")
    text = input("Enter text to append: ")

    with open(filename, "a") as file:
        file.write("\n" + text)

    with open(filename, "r") as file:
        print(file.read())


# 4. Count Characters
def count_characters():
    filename = input("Enter file name: ")

    with open(filename, "r") as file:
        data = file.read()

    print("Total characters:", len(data))


# 5. Count Lines
def count_lines():
    filename = input("Enter file name: ")

    with open(filename, "r") as file:
        lines = file.readlines()

    print("Total lines:", len(lines))


# 6. Count Words
def count_words():
    filename = input("Enter file name: ")

    with open(filename, "r") as file:
        data = file.read()

    words = data.split()
    print("Total words:", len(words))


# 7. Copy File
def copy_file():
    source = input("Enter source file: ")
    target = input("Enter target file: ")

    with open(source, "r") as file1:
        data = file1.read()

    with open(target, "w") as file2:
        file2.write(data)

    print("File copied successfully")


# 8. Search a Word
def search_word():
    filename = input("Enter file name: ")
    word = input("Enter word to search: ")

    with open(filename, "r") as file:
        data = file.read()

    if word in data:
        print("Word Found")
    else:
        print("Word Not Found")


# 9. Replace a Word
def replace_word():
    filename = input("Enter file name: ")
    old_word = input("Enter word to replace: ")
    new_word = input("Enter new word: ")

    with open(filename, "r") as file:
        data = file.read()

    data = data.replace(old_word, new_word)

    with open(filename, "w") as file:
        file.write(data)

    print("Word replaced successfully")


# 10. Find the Longest Line
def longest_line():
    filename = input("Enter file name: ")

    with open(filename, "r") as file:
        lines = file.readlines()

    longest = ""
    for line in lines:
        if len(line) > len(longest):
            longest = line

    print("Longest line:", longest.strip())


# 11. Remove Duplicate Lines
def remove_duplicate_lines():
    source = input("Enter source file: ")
    target = input("Enter target file: ")

    with open(source, "r") as file:
        lines = file.readlines()

    unique = []
    for line in lines:
        if line not in unique:
            unique.append(line)

    with open(target, "w") as file:
        file.writelines(unique)

    print("Duplicate lines removed")


# 12. Reverse File Contents
def reverse_file():
    filename = input("Enter file name: ")

    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines[::-1]:
        print(line.strip())


# 13. Merge Two Files
def merge_files():
    file1 = input("Enter first file: ")
    file2 = input("Enter second file: ")
    output = input("Enter output file: ")

    with open(file1, "r") as f1:
        data1 = f1.read()

    with open(file2, "r") as f2:
        data2 = f2.read()

    with open(output, "w") as f3:
        f3.write(data1 + "\n" + data2)

    print("Files merged successfully")


# 14. Student Record System
def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    course = input("Enter course: ")

    with open("students.txt", "a") as file:
        file.write(f"{roll},{name},{course}\n")

    print("Student added")


def view_students():
    try:
        with open("students.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No records found")


def search_student():
    roll = input("Enter roll number to search: ")
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == roll:
                    print("Roll:", data[0])
                    print("Name:", data[1])
                    print("Course:", data[2])
                    found = True
                    break
    except FileNotFoundError:
        print("No records found")
        return

    if not found:
        print("Student not found")


def student_system():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


# 15. Mini Notes App
def add_note():
    note = input("Enter note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added")


def view_notes():
    try:
        with open("notes.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No notes found")


def delete_notes():
    with open("notes.txt", "w") as file:
        file.write("")
    print("All notes deleted")


def notes_app():
    while True:
        print("\n1. Add Note")
        print("2. View Notes")
        print("3. Delete All Notes")
        print("4. Exit")

        # Fixed: original had a raw newline inside the string literal,
        # which causes a SyntaxError. Use "\n" instead.
        choice = input("Enter choice: \n")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    notes_app()
    # write_file()
    # read_file()
    # append_file()
    # count_characters()
    # count_lines()
    # count_words()
    # copy_file()
    # search_word()
    # replace_word()
    # longest_line()
    # remove_duplicate_lines()
    # reverse_file()
    # merge_files()
    # student_system()
