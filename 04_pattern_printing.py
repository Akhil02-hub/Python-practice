"""
Nested Loops and Pattern Printing
Topics: Square, Right Triangle, Inverted Triangle, Right-Aligned Triangle,
Full Pyramid, Inverted Pyramid, Hollow Square, Number Triangles
"""


# 1. Square Pattern
def square_pattern():
    n = int(input("Enter the number of rows: "))
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()


# 2. Right Triangle
def right_triangle():
    n = int(input("Enter the number of rows: "))
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()


# 3. Inverted Right Triangle
def inverted_right_triangle():
    n = int(input("Enter the number of rows: "))
    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            print("*", end="")
        print()


# 4. Right-Aligned Triangle
def right_aligned_triangle():
    n = int(input("Enter the number of rows: "))
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(" ", end="")
        for j in range(1, i + 1):
            print("*", end="")
        print()


# 5. Full Pyramid
def full_pyramid():
    n = int(input("Enter the number of rows: "))
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(" ", end="")
        for j in range(1, 2 * i):
            print("*", end="")
        print()


# 6. Inverted Full Pyramid
def inverted_full_pyramid():
    n = int(input("Enter the number of rows: "))
    for i in range(1, n + 1):
        for j in range(1, i):
            print(" ", end="")
        for j in range(1, 2 * (n - i) + 2):
            print("*", end="")
        print()


# 7. Hollow Square
def hollow_square():
    n = int(input("Enter the number of rows: "))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or i == n or j == 1 or j == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()


# 8. Number Triangle (1 / 1 2 / 1 2 3 ...)
def number_triangle():
    n = int(input("Enter the number of rows: "))
    for i in range(1, n + 1):
        for j in range(i):
            print(j + 1, end=" ")
        print()


# 9. Repeated Number Triangle (1 / 2 2 / 3 3 3 ...)
def repeated_number_triangle():
    n = int(input("Enter the number of rows: "))
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()


# 10. Continuous Number Triangle
def continuous_number_triangle():
    n = int(input("Enter the number of rows: "))
    number = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(number, end=" ")
            number += 1
        print()


# 11. Reverse Number Triangle
def reverse_number_triangle():
    n = int(input("Enter the number of rows: "))
    for i in range(1, n + 1):
        for j in range(i):
            print(i - j, end=" ")
        print()


if __name__ == "__main__":
    print("1. Square Pattern")
    print("2. Right Triangle")
    print("3. Inverted Right Triangle")
    print("4. Right Aligned Triangle")
    print("5. Full Pyramid")
    print("6. Inverted Full Pyramid")
    print("7. Hollow Square")
    print("8. Number Triangle")
    print("9. Repeated Number Triangle")
    print("10. Continuous Number Triangle")
    print("11. Reverse Number Triangle")

    choice = input("Choose: ")

    if choice == "1":
        square_pattern()
    elif choice == "2":
        right_triangle()
    elif choice == "3":
        inverted_right_triangle()
    elif choice == "4":
        right_aligned_triangle()
    elif choice == "5":
        full_pyramid()
    elif choice == "6":
        inverted_full_pyramid()
    elif choice == "7":
        hollow_square()
    elif choice == "8":
        number_triangle()
    elif choice == "9":
        repeated_number_triangle()
    elif choice == "10":
        continuous_number_triangle()
    elif choice == "11":
        reverse_number_triangle()
    else:
        print("Invalid choice")
