def heapify(arr, n, i):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and arr[largest] < arr[l]:
		largest = l

	if r < n and arr[largest] < arr[r]:
		largest = r

	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]

		heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range (n // 2, -1, -1):
        heapify(arr,n,i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr,i,0)

def findFromLarge(arr,k):
      n = len(arr)
      i = n - k

      heapSort(arr)

      print(arr[i])

A=[45,67,34,21,16,89,125,95,43]
n = len(A)

print('\nUnsorted array is')
for i in range(n):
    print(A[i])
print('\n-----------------------------')

heapSort(A)

print('\nSorted array is')
for i in range(n):
    print(A[i])
print('\n-----------------------------')

print('\n2nd largest element is')
findFromLarge(A,2)
print('\n-----------------------------')