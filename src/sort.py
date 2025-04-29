
def insertion_sort(array):
    """Function to perform insertion sort on a list."""
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def selection_sort(array):
    """Function to perform selection sort on a list."""
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

def merge_sort(array):
    """Function to perform merge sort on a list."""
    if len(array) > 1:
        mid = len(array) // 2
        L = array[:mid]
        R = array[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

    return array

def quick_sort(array):
    """Function to perform quick sort on a list."""
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def bubble_sort(array):
    """Function to perform bubble sort on a list."""
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


def stalin_sort(array):
    """Function to perform Stalin sort on a list."""
    if not array:
        return []

    sorted_array = [array[0]]
    for num in array[1:]:
        if num >= sorted_array[-1]:
            sorted_array.append(num)
    return sorted_array

if __name__ == "__main__":
    # Example usage
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", data)
    sorted_data = bubble_sort(data)
    print("Sorted array:", sorted_data)