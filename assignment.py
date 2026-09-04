#program to reverse a string without using slicing.

def reverse_string(text):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text


text = "python"
print(reverse_string(text))

def first_non_repeating(text):
    frequency = {}

 #Finding the first non - repeating character in a string.
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1


    for char in text:
        if frequency[char] == 1:
            return char

    return None

text = "programming"
print(first_non_repeating(text))