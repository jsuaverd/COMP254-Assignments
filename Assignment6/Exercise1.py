def linear_search(values, search_for):
    search_at = 0
    search_res = False

    while search_at < len(values) and search_res is False:
        if values[search_at] == search_for:
            search_res = True
        else:
            search_at = search_at + 1
    return search_res

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return False

A=[1,4,7,2,3,5,9] 
n = len(A)

print('\nArray values:\n')
for i in range(n):
    print(A[i])
print('\n-----------------------------')

k=2
print('\nSearching for ' + str(k) + ' in the array using linear search...')
print(linear_search(A,k))
print('\n-----------------------------')

l=5
print('\nSearching for ' + str(l) + ' in the array using binary search...')
print(binary_search(A,0,len(A)-1,l))
print('\n-----------------------------')

m=22
print('\nSearching for ' + str(m) + ' in the array using linear search...')
print(linear_search(A,m))
print('\n-----------------------------')

n=54
print('\nSearching for ' + str(n) + ' in the array using binary search...')
print(binary_search(A,0,len(A)-1,n))
print('\n-----------------------------')