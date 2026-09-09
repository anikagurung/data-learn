#program to reverse a string without using slicing.
def reversed_string(text):
    reversed_text=""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text
text = "python"
print(reversed_string(text))

#Find the first non-repeating character in a string.
#Example: Input: “programming” Output: “p”
def non_repeat():
    frequency = {}
    for text in input:
        if text in frequency:
            frequency[text] += 1

#Write a Python function to flatten a nested list.
def flatten_list(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            flattened = flatten_list(item)

            for value in flattened:
                result.append(value)
            else:
                result.append(item)
        return  result
numbers = [[1, 2], [3, 4], [5]]
print(flatten_list(numbers))

#Merge Two Sorted Lists
def merge_list (list1, list2):
    result = []
    i=0
    j=0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i+= 1
        else:
            result.append(list2[j])
            j+=1

    while i < len(list1):
        result.append(list1[i])
        i += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result

print(merge_list([1, 3, 5], [2, 4, 6]))

#Find All Pairs in a List that Sum to a Specific Value
def find_pairs(number, target):
    pairs =[]
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            if number[i] + number[j] == target:
                pairs.append((number[i], number[j]))
        return pairs
number = [1,2,3,4,5]
print(find_pairs(number, 6))
