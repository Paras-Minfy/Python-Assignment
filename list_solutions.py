# === Easy Question ===

# 1: List Operations
def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Easy Question 2: List Manipulation
def merge_sorted_lists(list1, list2):
    result = []
    i = j = 0
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

# === Medium Question ===

# 1: List Comprehensions
def generate_matrix(n, m):
    return [[i * j for j in range(m)] for i in range(n)]

# 2: Nested Lists
def transpose_matrix(matrix):
    if not matrix or not matrix[0]:
        return []
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# === Hard Question ===

# 1: Advanced List Operations
def find_peaks(numbers):
    peaks = []
    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            peaks.append(i)
    return peaks

# Hard Question 2: List Algorithms
def rotate_list(nums, k):
    n = len(nums)
    if n == 0:
        return []
    k = k % n
    def reverse(sublist, start, end):
        while start < end:
            sublist[start], sublist[end] = sublist[end], sublist[start]
            start += 1
            end -= 1
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    return nums

# Test Cases
if __name__ == "__main__":
    # Test filter_even_numbers
    print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  
    print(filter_even_numbers([1, 3, 5]))        

    # Test merge_sorted_lists
    print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  
    print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))  

    # Test generate_matrix
    print(generate_matrix(3, 3))

    # Test transpose_matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(transpose_matrix(matrix))

    # Test find_peaks
    print(find_peaks([1, 3, 2, 3, 5, 4, 3, 2, 3, 1]))  

    # Test rotate_list
    print(rotate_list([1, 2, 3, 4, 5], 2))  
    print(rotate_list([1, 2, 3], 4))        
 