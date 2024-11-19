from collections import deque

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

q1 = deque([123, 45, 1089, 3, 345, 87, 23, 56, 247])

arr = list(q1)
quicksort(arr, 0, len(arr) - 1)

sorted_queue = deque(arr)

print('Sorted queue:')
for x in sorted_queue:
    print(x, end=" ")
