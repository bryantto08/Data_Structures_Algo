# Quicksort Algorithm
# Quicksort: Using a Pivot to separate elements less than pivot from elements greater than pivot
# Important Note: Time Complexity of Quicksort relies HEAVILY on picking the right pivot
def quicksort(array):
    if len(array) < 2:  # Base Case: If length of array equals 1 or 0
        return array
    pivot = array[0]  # Pivot used
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)  # Then recursively calling it until it reaches base case

array = [6, 43, 2, 9, 5, 10]
a = quicksort(array)
print(a)
