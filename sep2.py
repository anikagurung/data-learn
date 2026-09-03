#function to flatten a nested list

def flatten_list(nested_list):
    result = []
    for sublist in nested_list:
        for item in sublist:
            result.append(item)
    return result
numbers = [[1,2], [3,4], [5]]
print(flatten_list(numbers))

#function to merge two sorted lists into a single sorted list.
#Input: [1, 3, 5], [2, 4, 6]
def merge_sortedlists(list1, list2):
    result = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result.extend(list1[i:])
    result.extend(list2[j:])

    return result
list1 = [1, 3, 5]
list2 = [2, 4, 6]

print(merge_sortedlists(list1, list2))

#function to find all pairs in a list that sum to a specific value.
def find_pairs(numbers, target):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))

    return pairs


numbers = [1, 2, 3, 4, 5]

print(find_pairs(numbers, 6))