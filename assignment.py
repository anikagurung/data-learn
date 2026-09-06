#q1program to reverse a string without using slicing.

def reverse_string(text):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text
text = "python"
print(reverse_string(text))

def first_non_repeating(text):
    frequency = {}

 #q2Finding the first non - repeating character in a string.
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

#q3Check if a string is a palindrome.
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
#q4Count the frequency of each character in a string.
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

#q5Remove duplicate characters from a string while preserving order.
text = "programming"

result = ""
seen = ""

for char in text:
    if char not in seen:
        result += char
        seen += char

print(result)
#Q6 Remove duplicates from a list without using set().
numbers = [1, 2, 2, 3, 4, 4]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print(result)
#q7Find the second largest number in a list.

numbers = [10, 20, 5, 30, 25]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)

#Q8. Find all duplicate elements in a list
numbers = [1, 2, 3, 2, 4, 5, 1]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(duplicates)

#Q9. Rotate a list by K position
numbers = [1, 2, 3, 4, 5]
k = 2
k = k % len(numbers)
result = numbers[-k:] + numbers[:-k]
print(result)

#Q10. Find the intersection of two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = []

for num in list1:
    if num in list2:
        result.append(num)

print(result)
#q11Count frequency of elements in a list using a dictionary
numbers = [1, 2, 2, 3, 3, 3]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1

print(frequency)

#q12Find the key having the maximum value.
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

#q13Reverse a dictionary.

def reverse_dictionary(data):
    reversed_dict = {}

    for key in data:
        value = data[key]
        reversed_dict[value] = key
    return reversed_dict
data = {"a": 1, "b": 2}
print(reverse_dictionary(data))


#q14Merge two dictionaries.
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


#q15Count word frequency in a sentence using dictionary.
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

