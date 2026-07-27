"""
Python Functions Handbook
Topics: def, parameters vs arguments, return vs print, nested functions
"""


# 1. Hello
def hello():
    print('Hello World')


# 2. Square
def square(n):
    return n * n


# 3. Even/Odd
def check(n):
    return 'Even' if n % 2 == 0 else 'Odd'


# 4. Greater
def bigger(a, b):
    return a if a > b else b


# 5. Factorial
def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


# 6. Prime
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 7. List Sum
def list_sum(lst):
    t = 0
    for i in lst:
        t += i
    return t


# 8. Largest
def largest(lst):
    m = lst[0]
    for i in lst:
        if i > m:
            m = i
    return m


# 9. Second Largest
def second_largest(lst):
    largest_val = second_val = lst[0]
    for i in lst[1:]:
        if i > largest_val:
            second_val = largest_val
            largest_val = i
        elif i > second_val and i != largest_val:
            second_val = i
    return second_val


# 10. Reverse List
def rev(lst):
    r = []
    for i in range(len(lst) - 1, -1, -1):
        r.append(lst[i])
    return r


# 11. Unique
def unique(lst):
    u = []
    for i in lst:
        if i not in u:
            u.append(i)
    return u


# 12. Merge
def merge(lst1, lst2):
    result = []
    for i in lst1:
        result.append(i)
    for i in lst2:
        result.append(i)
    return result


# 13. Count Even/Odd
def count_even_odd(lst):
    even = odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


# 14. Largest & Smallest
def largest_smallest(lst):
    max_val = min_val = lst[0]
    for i in lst:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
    return max_val, min_val


# 15. Average
def average(lst):
    return sum(lst) / len(lst)


# 16. Vowel Count
def vowel_count(s):
    c = 0
    for ch in s:
        if ch in 'aeiouAEIOU':
            c += 1
    return c


# 17. Nested Return (cube calls square)
def cube(n):
    return square(n) * n


if __name__ == "__main__":
    hello()
    print(square(5))
    print(check(7))
    print(bigger(3, 9))
    print(fact(5))
    print(prime(17))
    print(list_sum([1, 2, 3]))
    print(largest([4, 9, 2]))
    print(second_largest([4, 9, 2, 9]))
    print(rev([1, 2, 3]))
    print(unique([1, 2, 1, 3]))
    print(merge([1, 2], [3, 4]))
    print(count_even_odd([1, 2, 3, 4]))
    print(largest_smallest([4, 9, 2]))
    print(average([1, 2, 3]))
    print(vowel_count("Hello World"))
    print(cube(3))
