#q16
for i in range(1):
    print("●", end="      ")

    for j in range(2):
        print("*", end="")

#Print multiplication table of a given number.
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
#Find factorial using for loop. 5

numb = int(input("Enter a number: "))

factorial = 1

for i in range(1, numb + 1):
    factorial = factorial * i

print(factorial)
#Find all prime numbers between 1 and 100.
for number in range(2, 101):
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number)

#Generate Fibonacci series up to N terms.
n = int(input("Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a)

    c = a + b
    a = b
    b = c


# Q21. Find the first non-repeating number in a list

numbers = [1, 2, 3, 4, 5, 1, 2, 3]

for num in numbers:
    if numbers.count(num) == 1:
        print("Q21:", num)
        break


# Q22. Find the Nth non-repeating number in a list

numbers = [1, 2, 3, 4, 5, 1, 2, 3]
N = 2

count = 0

for num in numbers:
    if numbers.count(num) == 1:
        count += 1

        if count == N:
            print("Q22:", num)
            break


# Q23. Check whether two strings are anagrams

word1 = "listen"
word2 = "silent"

if sorted(word1) == sorted(word2):
    print("Q23:", True)
else:
    print("Q23:", False)


# Q24. Find missing number from array

numbers = [1, 2, 3, 5]

for num in range(1, 6):
    if num not in numbers:
        print("Q24:", num)


# Q25. Find top occurring element in a list

numbers = [1, 2, 2, 3, 3, 3, 4]

top = numbers[0]

for num in numbers:
    if numbers.count(num) > numbers.count(top):
        top = num

print("Q25:", top)


# BONUS 1. List vs Tuple

# List can be changed
my_list = [1, 2, 3]
my_list[0] = 10
print("List:", my_list)

# Tuple cannot be changed
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)


# BONUS 2. Dictionary vs Set

# Dictionary stores key-value pairs
student = {
    "name": "Anika",
    "age": 24
}
print("Dictionary:", student)

# Set stores unique values
numbers_set = {1, 2, 3, 3, 4}
print("Set:", numbers_set)


# BONUS 3. Shallow Copy vs Deep Copy

import copy

original = [[1, 2], [3, 4]]

# Shallow copy
shallow = copy.copy(original)

# Deep copy
deep = copy.deepcopy(original)

print("Original:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)


# BONUS 4. is vs ==

a = [1, 2]
b = [1, 2]

# == checks values
print("a == b:", a == b)

# is checks whether they are the same object
print("a is b:", a is b)


# BONUS 5. append() vs extend()

numbers = [1, 2, 3]

# append() adds one item
numbers.append(4)
print("After append:", numbers)

# extend() adds multiple items
numbers.extend([5, 6])
print("After extend:", numbers)