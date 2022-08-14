# Find the min subarray greater than or equal to given sum

import math

def find_subarray(array, k):
    min_size = math.inf
    curr_value = 0
    window_start = 0  # Start of the Dynamic Window

    # i in the End of the Dynamic Window
    for i in range(len(array)):
        curr_value += array[i]

        while curr_value >= k:
            min_size = min(min_size, i - window_start + 1)  # i - window_start + 1 is current window size
            curr_value -= array[window_start]
            window_start += 1

    return min_size

a = [4, 2, 2, 7, 1, 2]
print(find_subarray(a, 8))