# Mergesort Algorithm

def mergesort(array):
    if len(array) == 1:  # Base Case
        return array
    if len(array) > 1:
        # Recursive Case
        left_array = array[:len(array)//2]  # Recursively Splitting
        right_array = array[len(array)//2:]
        mergesort(left_array)
        mergesort(right_array)

        # Merging Implementation
        i = 0  # Left Array Index
        j = 0  # Right Array Index
        k = 0  # Merged Array Index
        while i < len(left_array) and j < len(right_array):  # While BOTH of the indices are less than array length
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):  # If Right array is completed but left array still has elements
            array[k] = left_array[i]
            k += 1
            i += 1

        while j < len(right_array):  # If Left array is completed but right array still has elements
            array[k] = right_array[j]
            k += 1
            j += 1


arr = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
mergesort(arr)
print(arr)

