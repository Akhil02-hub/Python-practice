"""
Python Basics and Control Flow
Topics: Input/Output, Variables, Data Types, Type Casting, Operators,
if/elif/else, while loop, for loop
"""


# 1. Check Even or Odd
def check_even_odd():
    num = int(input("Enter the number: "))
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")


# 2. Check Positive / Negative / Zero
def check_sign():
    num = int(input("Enter the number: "))
    if num > 0:
        print("Positive Number")
    elif num < 0:
        print("Negative Number")
    else:
        print("Zero")


# 3. Multiplication Table
def multiplication_table():
    num = int(input("Enter the number: "))
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)


# 4. Sum from 1 to n
def sum_to_n():
    n = int(input("Enter the number: "))
    total = 0
    for i in range(1, n + 1):
        total += i
    print("Sum is", total)


# 5. Count Even Numbers from 1 to n
def count_even_numbers():
    n = int(input("Enter the number: "))
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            count += 1
    print("Even numbers:", count)


# 6. Factorial
def factorial():
    num = int(input("Enter the number: "))
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print("Factorial is", fact)


if __name__ == "__main__":
    print("1. Check Even Odd")
    print("2. Check Sign")
    print("3. Multiplication Table")
    print("4. Sum to N")
    print("5. Count Even Numbers")
    print("6. Factorial")

    choice = input("Choose: ")

    if choice == "1":
        check_even_odd()
    elif choice == "2":
        check_sign()
    elif choice == "3":
        multiplication_table()
    elif choice == "4":
        sum_to_n()
    elif choice == "5":
        count_even_numbers()
    elif choice == "6":
        factorial()
    else:
        print("Invalid choice")

