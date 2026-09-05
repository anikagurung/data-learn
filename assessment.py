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
