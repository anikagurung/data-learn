#Write a Python function to reverse a given string.
def reverse_string(text):
    return text[::-1]
result = reverse_string("Hello")
print(result)


def reversed_string(txt):
    reversed_text = ""
    for char in txt:
        reversed_text = char + reversed_text
    return reversed_text
txt = "Hello"
print(reversed_string(txt))


def check_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    char_count = {}
    for char in string1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char  in string2:
        if char not in char_count:
            return False

        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    return True
print(check_anagram("listen", "silent"))

# Write a Python function to find the sum of all numbers in a list.
def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers = [10, 20, 30, 40]
print(sum_numbers(numbers))