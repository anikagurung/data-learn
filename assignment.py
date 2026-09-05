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

#Check if a string is a palindrome.
def is_palinrome(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text;
    if text == reversed_text:
        return True
    else:
        return False
text = "madam"
print(is_palinrome(text))

#def is_palindrome_simple(text):
  #  return text == text[::-1]

#print(is_palindrome_simple("madam"))
#Count the frequency of each character in a string.
def count_frequency(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    return frequency
numbers = [1, 2, 2, 3, 3, 3]
print(count_frequency(numbers))
#Find the key having the maximum value.
def find_max_key(data):
    max_value = 0
    max_key = ""
    for key in data:
        if data[key] > max_value:
            max_value = data[key]
            max_key = key

    return max_key

data = {"A": 100, "B": 500, "C": 300}
print(find_max_key(data))

#Reverse a dictionary.

def reverse_dictionary(data):
    reversed_dict = {}

    for key in data:
        value = data[key]
        reversed_dict[value] = key
    return reversed_dict
data = {"a": 1, "b": 2}
print(reverse_dictionary(data))


#Merge two dictionaries.
def merge_dictionaries(d1, d2):
    merged = {}
    for key in d1:
        merged[key] = d1[key]
    for key in d2:
        merged[key] = d2[key]
    return merged
d1 = {"a": 1}
d2 = {"b": 2}
print(merge_dictionaries(d1, d2))


#Count word frequency in a sentence using dictionary.
def word_frequency(sentence):
    frequency = {}

    words = sentence.split()

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency
sentence = "python is good python is easy"
print(word_frequency(sentence))