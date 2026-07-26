"""
15 String Programs in Python
Topics: length, vowels/consonants, case count, reverse, palindrome,
word count, longest word, anagram, first non-repeating char,
max occurring char, substring search, frequency, rotation,
remove consecutive duplicates
"""


# Q1. Count Length
def count_length(s):
    c = 0
    for i in s:
        c += 1
    return c


# Q2. Count Vowels
def count_vowels(s):
    c = 0
    for i in s:
        if i in 'aeiouAEIOU':
            c += 1
    return c


# Q3. Count Consonants
def count_consonants(s):
    c = 0
    for i in s:
        if i.isalpha() and i not in 'aeiouAEIOU':
            c += 1
    return c


# Q4. Upper & Lower Count
def upper_lower_count(s):
    u = l = 0
    for i in s:
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1
    return u, l


# Q5. Reverse String
def reverse_string(s):
    r = ''
    for i in range(len(s) - 1, -1, -1):
        r += s[i]
    return r


# Q6. Palindrome Check
def is_palindrome(s):
    r = ''
    for i in range(len(s) - 1, -1, -1):
        r += s[i]
    return 'Palindrome' if r == s else 'Not Palindrome'


# Q7. Count Words
def count_words(s):
    if s == '':
        return 0
    c = 1
    for i in s:
        if i == ' ':
            c += 1
    return c


# Q8. Longest Word
def longest_word(s):
    word = longest = ''
    for ch in s:
        if ch != ' ':
            word += ch
        else:
            if len(word) > len(longest):
                longest = word
            word = ''
    if len(word) > len(longest):
        longest = word
    return longest


# Q9. Anagram Check
def is_anagram(a, b):
    if len(a) != len(b):
        return 'Not Anagram'
    for x in a:
        c1 = c2 = 0
        for i in a:
            if i == x:
                c1 += 1
        for j in b:
            if j == x:
                c2 += 1
        if c1 != c2:
            return 'Not Anagram'
    return 'Anagram'


# Q10. First Non-Repeating Character
def first_non_repeating(s):
    for i in s:
        c = 0
        for j in s:
            if i == j:
                c += 1
        if c == 1:
            return i
    return 'No unique character'


# Q11. Max Occurring Character
def max_occurring_char(s):
    max_count = 0
    max_char = ''
    for i in s:
        c = 0
        for j in s:
            if i == j:
                c += 1
        if c > max_count:
            max_count = c
            max_char = i
    return max_char


# Q12. Substring Search (manual, no find()/in)
# FIXED: original had "def f(a,b): for i in range(...)" on one line,
# which is a syntax error. Split into proper function body below.
def find_substring(a, b):
    for i in range(len(a) - len(b) + 1):
        ok = True
        for j in range(len(b)):
            if a[i + j] != b[j]:
                ok = False
                break
        if ok:
            return 'Found'
    return 'Not Found'


# Q13. Character Frequency
def char_frequency(s):
    visited = ''
    for i in s:
        if i not in visited:
            c = 0
            for j in s:
                if i == j:
                    c += 1
            print(i, '=', c)
            visited += i


# Q14. Rotation Check
def is_rotation(a, b):
    if len(a) != len(b):
        return 'Not Rotation'
    t = a + a
    for i in range(len(t) - len(b) + 1):
        if t[i:i + len(b)] == b:
            return 'Rotation'
    return 'Not Rotation'


# Q15. Remove Consecutive Duplicates
def remove_consecutive_duplicates(s):
    if s == '':
        return ''
    r = s[0]
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            r += s[i]
    return r


if __name__ == "__main__":
    print(count_length("hello"))
    print(count_vowels("hello world"))
    print(count_consonants("hello world"))
    print(upper_lower_count("Hello World"))
    print(reverse_string("hello"))
    print(is_palindrome("madam"))
    print(count_words("hello world foo"))
    print(longest_word("the quick brown fox"))
    print(is_anagram("listen", "silent"))
    print(first_non_repeating("swiss"))
    print(max_occurring_char("mississippi"))
    print(find_substring("hello world", "wor"))
    char_frequency("banana")
    print(is_rotation("waterbottle", "erbottlewat"))
    print(remove_consecutive_duplicates("aaabbbccd"))
