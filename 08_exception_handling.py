"""
Exception Handling Practice
Topics: try/except, else/finally, multiple exceptions, raise,
custom-style exceptions, file handling, IndexError, KeyError
"""


# 1. ZeroDivisionError
def zero_division_error():
    try:
        a = int(input("enter a: "))
        b = int(input("enter b: "))
        print("division is:", a / b)
    except ZeroDivisionError:
        print("cannot divided by 0")


# 2. ValueError
def value_error():
    try:
        a = int(input("Enter a number: "))
        print("You entered:", a)
    except ValueError:
        print("Invalid input")


# 3. IndexError
def index_error():
    try:
        nums = list(map(int, input("enter the list: ").split()))
        a = int(input("enter the index: "))
        print(f"the element in that index is:", nums[a])
    except IndexError:
        print("please enter the valid index !")


# 4. KeyError
def key_error():
    try:
        student = {
            "name": "Akhil",
            "age": 18,
            "course": "CSE"
        }
        key = input("Please enter the key: ")
        print(student[key])
    except KeyError:
        print("Error! please enter the valid key")


# 5. File handling - FileNotFoundError
def file_not_found_error():
    try:
        file = input("Enter file name: ")
        f = open(file, "r")
        print("\nFile Contents:\n")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("File not found")


# 6. try/except/else
def division_with_else():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by 0")
    except ValueError:
        print("Invalid input")
    else:
        print("Division successful")
        print("Division is:", result)


# 7. Multiple except blocks
def multiple_exceptions():
    try:
        a = int(input("Enter the number: "))
        b = int(input("Enter the number: "))
        print("Division is:", a / b)
    except ZeroDivisionError:
        print("Error! Cannot divide by 0")
    except ValueError:
        print("Please enter a valid number")


# 8. try/except/else/finally combined
def exception_else_finally():
    try:
        a = int(input("enter the number: "))
        b = int(input("enter the number: "))
        c = a / b
    except ZeroDivisionError:
        print("Error! cannot divide with 0")
    except ValueError:
        print("please enter the number")
    else:
        print("Division successful")
        print("division is:", c)
    finally:
        print("Program finished")


# 9. raise - age eligibility check
def check_age():
    try:
        age = int(input("enter the age: "))
        if age < 18:
            raise ValueError('age must be 18 or greater')
        print("Eligible")
    except ValueError as e:
        print(e)


# 10. raise - password validation
def password_check():
    try:
        password = input("Enter password: ")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        print("Password accepted")
    except ValueError as e:
        print(e)


# 11. raise - custom-style exception (bank withdrawal)
class InsufficientBalanceError(Exception):
    pass


def bank_withdrawal():
    try:
        balance = float(input("Enter balance: "))
        amount = float(input("Enter withdrawal amount: "))
        if amount > balance:
            raise InsufficientBalanceError("Insufficient balance")
        print("Transaction Successful")
    except InsufficientBalanceError as e:
        print(e)


# 12. File handling with finally
def file_opener():
    try:
        file = input("Enter file name: ")
        f = open(file, "r")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("File not found")
    finally:
        print("File operation completed")


# 13. raise - marks validation
def marks_validator():
    try:
        marks = int(input("Enter marks: "))
        if marks < 0 or marks > 100:
            raise ValueError("Invalid marks")
        print("Marks accepted")
    except ValueError as e:
        print(e)


# 14. IndexError + ValueError together
def safe_list_access():
    try:
        nums = list(map(int, input("Enter numbers: ").split()))
        index = int(input("Enter index: "))
        if index < 0 or index >= len(nums):
            raise IndexError("Invalid index")
        print("Element:", nums[index])
    except IndexError as e:
        print(e)
    except ValueError:
        print("Invalid input")


# 15. Full try/except/else/finally - calculator
def calculator():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /): ")

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b
        else:
            raise ValueError("Invalid operator")

    except ValueError as e:
        print(e)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print("Result:", result)
    finally:
        print("Program ended")


if __name__ == "__main__":
    calculator()
    # zero_division_error()
    # value_error()
    # index_error()
    # key_error()
    # file_not_found_error()
    # division_with_else()
    # multiple_exceptions()
    # exception_else_finally()
    # check_age()
    # password_check()
    # bank_withdrawal()
    # file_opener()
    # marks_validator()
    # safe_list_access()
