"""
15 List Programs in Python
Topics: create/print lists, traversal, sum, largest/smallest,
even/odd count, search, count, reverse, duplicates, merge,
second largest, palindrome check
"""


# 1. Store and print a list
def print_list():
    nums = [1, 2, 3, 4, 5]
    print(nums)


# 2. Take n numbers from the user
def input_list():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(nums)


# 3. Print all elements one by one
def traverse_list():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    for i in nums:
        print(i)


# 4. Sum of all elements
def list_sum():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    total = 0
    for i in nums:
        total += i
    print("Sum =", total)


# 5. Largest element without max()
def find_largest():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    largest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
    print("Largest =", largest)


# 6. Smallest element without min()
def find_smallest():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    smallest = numbers[0]
    for i in numbers:
        if i < smallest:
            smallest = i
    print("Smallest =", smallest)


# 7. Count even numbers
def count_even():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    c = 0
    even = []
    for i in nums:
        if i % 2 == 0:
            c += 1
            even.append(i)
    print("No. of even numbers:", c)
    print("Even numbers are:", even)


# 8. Count odd numbers
def count_odd():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    c = 0
    odd = []
    for i in nums:
        if i % 2 != 0:
            c += 1
            odd.append(i)
    print("No. of odd numbers:", c)
    print("Odd numbers are:", odd)


# 9. Search for an element manually
def search_element():
    items = ["phone", "laptop", "pc", "airbuds"]
    n = input("Enter the item to search: ")
    for ind, i in enumerate(items):
        if i == n:
            print("Available at:", ind)
            break
    else:
        print("Not available")


# 10. Count occurrences of an element
def count_occurrences():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    n = int(input("Enter the number to search: "))
    count = 0
    for i in nums:
        if n == i:
            count += 1
    if count == 0:
        print(f"{n} does not appear in the list")
    else:
        print(f"{n} repeated {count} times")


# 11. Reverse a list without reverse() or slicing
def reverse_list():
    nums = [1, 2, 3, 4, 5, 6]
    for i in range(len(nums) - 1, -1, -1):
        print(nums[i], end=" ")


# 12. Remove duplicate elements
def remove_duplicates():
    nums = [1, 2, 3, 1, 1, 3]
    unique = []
    for i in nums:
        if i not in unique:
            unique.append(i)
    print("Unique elements:", unique)


# 13. Merge two lists
def merge_lists():
    num1 = [1, 2]
    num2 = [3, 4]
    num3 = []
    for i in num1:
        num3.append(i)
    for i in num2:
        num3.append(i)
    print(num3)


# 14. Second largest element
# Note: if all elements are equal, this returns that same value (edge case)
def second_largest():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    largest = nums[0]
    second = nums[0]
    for i in nums[1:]:
        if i > largest:
            second = largest
            largest = i
        elif i > second and i != largest:
            second = i
    print("Second largest:", second)


# 15. Check whether a list is a palindrome
def is_palindrome():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    reverse = []
    for i in range(len(nums) - 1, -1, -1):
        reverse.append(nums[i])
    if reverse == nums:
        print("Palindrome")
    else:
        print("Not a palindrome")


if __name__ == "__main__":
    print_list()
    reverse_list()
    print()
    remove_duplicates()
    merge_lists()
    # input_list()
    # traverse_list()
    # list_sum()
    # find_largest()
    # find_smallest()
    # count_even()
    # count_odd()
    # search_element()
    # count_occurrences()
    # second_largest()
    # is_palindrome()
