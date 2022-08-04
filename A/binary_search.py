# Python Implementation of a Binary Search

def binary_search(list1, a):
    high = len(list1) - 1  # High = Highest index of list
    low = 0  # Low  = First index in list
    while low <= high:  # While lowest index is lower or equal to the highest index
        mid = (high + low) // 2  # Mid = midpoint index between low and high
        if list1[mid] == a:
            return mid
        if list1[mid] < a:  # If list value < a, the lowest index becomes the current midpoint
            low = mid + 1
        if list1[mid] > a:  # If list value > a, the highest index becomes the current midpoint
            high = mid - 1
    return None


test = [1, 3, 5, 7, 9, 23, 35, 89]
print(binary_search(test, 19))

