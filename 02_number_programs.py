"""
Number Programs
Topics: Reverse Number, Count Digits, Prime, Palindrome, Armstrong,
Perfect Number, Strong Number
"""


# 1. Reverse Number
def reverse_number():
    num = int(input("Enter the number: "))
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    print("Reversed number is:", reverse)


# 2. Count Digits
def count_digits():
    num = int(input("Enter the number: "))
    if num == 0:
        print("No. of digits is 1")
    else:
        total = 0
        while num != 0:
            num = num // 10
            total += 1
        print("No. of digits is", total)


# 3. Prime Number (fixed: now checks only up to sqrt(n), not n)
def is_prime():
    n = int(input("Enter the number: "))
    if n <= 1:
        print("Not a Prime Number")
        return
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not a Prime Number")
            return
    print("Prime Number")


# 4. Palindrome Number
def palindrome_number():
    num = int(input("Enter the number: "))
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    if original == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")


# 5. Armstrong Number
def armstrong_number():
    num = int(input("Enter the number: "))
    original = num
    total = 0
    power = len(str(num))
    while num > 0:
        digit = num % 10
        total += digit ** power
        num = num // 10
    if original == total:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")


# 6. Perfect Number
def perfect_number():
    num = int(input("Enter the number: "))
    original = num
    i = 1
    total = 0
    while i < num:
        if num % i == 0:
            total += i
        i += 1
    if total == original:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")


# 7. Strong Number
def strong_number():
    num = int(input("Enter the number: "))
    original = num
    sum_fact = 0
    while num > 0:
        digit = num % 10
        fact = 1
        for i in range(1, digit + 1):
            fact *= i
        sum_fact += fact
        num = num // 10
    if sum_fact == original:
        print("Strong Number")
    else:
        print("Not a Strong Number")


if __name__ == "__main__":
    is_prime()
    # reverse_number()
    # count_digits()
    # palindrome_number()
    # armstrong_number()
    # perfect_number()
    # strong_number()
