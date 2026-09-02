#Write a Python function to find the maximum and minimum elements in a given list.
#Input: [3, 1, 4, 1, 5, 9]


def find_maxmin(numbers):
    maximum = numbers[0]
    minimum = numbers[0]

    for x in numbers:
        if x > maximum:
            maximum = x

        if x < minimum:
            minimum = x

    return maximum, minimum


numbers = [3, 1, 4, 1, 5, 9]

maximum, minimum = find_maxmin(numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)

#Remove Duplicates from a List
#Write a Python function to remove duplicates from a list while preserving the order.

def remove_duplicates(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)

    return result
numbers = [1, 2, 2, 3, 4, 4, 5]

print(remove_duplicates(numbers))

#Write a Python function to find the intersection of two lists.
#Input: [1, 2, 3, 4], [3, 4, 5, 6]
def find_intersection(list1, list2):
    output = []

    for num in list1:
        if num in list2 and num not in output:
            output.append(num)
    return output
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(find_intersection(list1, list2))