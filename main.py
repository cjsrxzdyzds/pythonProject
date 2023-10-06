import time
import random
# import math
# from typing import List

n = 100
# Sum = 0
# random_array = []
# shift_count = 0

brew_start = time.time()

random_array = [random.randint(1, 100000) for _ in range(n)]
print("Random Array:", random_array)
sorted_array = sorted(random_array)
print("Sorted Array:", sorted_array)


def generate_circularly_shifted_array(sorted_array, shift_count):
    n = len(sorted_array)
    # Handle the case where the shift count is greater than the array length
    shift_count = shift_count % n
    # Create a new array to store the circularly shifted elements
    circularly_shifted_array = [0] * n
    # Copy elements to the circularly shifted array based on the shift count
    for i in range(n):
        circularly_shifted_array[i] = sorted_array[(i + (n - shift_count)) % n]

    return circularly_shifted_array


# Example usage:
length_count = (len(sorted_array) - 1)
shift_count = random.randint(1, length_count)
circularly_shifted_array = generate_circularly_shifted_array(sorted_array, shift_count)
print("Shifted Array:", circularly_shifted_array)

brew_end = time.time()
brew_time = brew_end - brew_start


# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         for k in range(j, n + 1):
#             Sum += i * j * k
#             if j == 2 * i:
#                 j = n

# start_time = time.time()

A = circularly_shifted_array


def find_max_in_circularly_shifted_array_recursive(A, left, right):
    # Base case: If the search space has narrowed down to a single element, return it.
    if left == right:
        return A[left]

    mid = (left + right) // 2

    # Compare the middle element with the rightmost element to determine the search direction.
    if A[mid] > A[right]:
        # If the middle element is greater, search in the right half.
        return find_max_in_circularly_shifted_array_recursive(A, mid + 1, right)
    elif A[mid] < A[right]:
        # If the middle element is smaller, search in the left half.
        return find_max_in_circularly_shifted_array_recursive(A, left, mid)
    else:
        # If there's a tie, search in both halves.
        left_max = find_max_in_circularly_shifted_array_recursive(A, left, mid)
        right_max = find_max_in_circularly_shifted_array_recursive(A, mid + 1, right)
        return max(left_max, right_max)


# Wrapper function to initiate the recursive search.
def find_max_in_circularly_shifted_array(A):
    return find_max_in_circularly_shifted_array_recursive(A, 0, len(A) - 1)


# Example usage:
# A = circularly_shifted_array
result = find_max_in_circularly_shifted_array(A)
print("The largest element is:", result)

# end_time = time.time()
# elapsed_time = end_time - start_time

finalStartTime = time.perf_counter_ns()


def find_largest_circular_shifted_element(circularly_shifted_array):
    left, right = 0, len(circularly_shifted_array) - 1

    while left < right:
        mid = (left + right) // 2

        if circularly_shifted_array[mid] > circularly_shifted_array[right]:
            left = mid + 1
        else:
            right = mid

    return circularly_shifted_array[left - 1]


finalEndTime = time.perf_counter_ns()
finalRunTime = finalEndTime - finalStartTime


resultNew = find_largest_circular_shifted_element(circularly_shifted_array)
print("The new largest element is:", resultNew)

print(f"Brew-time: {brew_time} seconds")
# print(f"Run-time: {elapsed_time} seconds")
print(finalRunTime)
print(f"Final-time: {finalRunTime} seconds")
