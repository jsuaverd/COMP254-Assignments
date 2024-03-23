def linear_search(values, search_for):
    search_at = 0
    search_res = False

    while search_at < len(values) and search_res is False:
        if values[search_at] == search_for:
            search_res = True
        else:
            search_at = search_at + 1
    return search_res

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