# Find the max sum subarray of fixed length k
# Example Input: [4, 2, 1, 7, 8, 1, 2, 8, 1, 0] - > 16
import math

# This is a fixed Sliding Window Example
def find_max(array, k):
    max_value = -1000
    curr_value = 0

    for i in range(len(array)):  # Iterating through array, Sliding Window should be O(n) time
        curr_value += array[i]  # curr_value IS the sliding window, adds next index value
        if i >= (k - 1):
            max_value = max(max_value, curr_value)
            # If Sliding Window is length (k-1), subtract previous index so that the sliding window stays the same
            # length
            curr_value -= array[i - (k - 1)]

    return max_value


a = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
print(find_max(a, 3))
