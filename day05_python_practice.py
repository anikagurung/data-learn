
# Day 05 - Python Practice Exercises

# 1. Find the largest number in a list without using max()
numbers = [12, 45, 23, 67, 34]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)


# 2. Count vowels in a string
text = "programming is interesting"
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)


# 3. Check whether a string is a palindrome
word = "madam"
reversed_word = ""

for char in word:
    reversed_word = char + reversed_word

if word == reversed_word:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")


# 4. Find duplicate elements in a list
numbers = [1, 2, 3, 2, 4, 5, 3, 6]
duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate elements:", duplicates)


# 5. Calculate the sum of even numbers
numbers = [10, 15, 20, 25, 30]
total = 0

for num in numbers:
    if num % 2 == 0:
        total += num

print("Sum of even numbers:", total)
