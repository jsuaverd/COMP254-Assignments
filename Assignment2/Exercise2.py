#The difference between a shallow copy and a deep copy is that in a shallow copy, we create a new collection and populate it with REFERENCES to child objects from the original. This means that any changes made to the copy also reflects on the original, and vice versa. Whereas in a deep copy, we create a new collection and recursively creates copies of the objects from the original. This means that the original and the copy are independent of each other and any changes made on either do not reflect on the other.


# importing the module
from numpy import array

print('\nSHALLOW COPY --------------------------------------------------------------------------')
#Shallow copy-----------------------------------------------------------------------------
# creating the first array
arr1 = array(['ant', 'bat', 'cat', 'dog', 'emu'])
# displaying the identity of arr1
print('\nArray 1 (ID:' +  str(id(arr1)) + '):')
for item in arr1:
    print(item)
print('--------------------------------------------------------------------------')
# shallow copy arr1 in arr2 using view()
arr2 = arr1.view()
# displaying the identity of arr2
print('\nArray 2 (Copy of Array 1) (ID:' +  str(id(arr2)) + '):')
for item in arr2:
    print(item)
print('--------------------------------------------------------------------------')
# making a change in arr1
arr1[3] = 'bee'
# displaying the arrays
print('\nAfter making a change in Array 1:')
print('\nArray 1:')
for item in arr1:
    print(item)
print('--------------------------------------------------------------------------')
print('\nArray 2 (Copy of Array 1):')
for item in arr2:
    print(item)


print('\nDEEP COPY --------------------------------------------------------------------------')
#Deep copy-----------------------------------------------------------------------------
# creating the first array
arr3 = array([1001,2002,3003,4004,5005,6006])
# displaying the identity of arr3
print('\nArray 3 (ID:' +  str(id(arr3)) + '):')
for item in arr3:
    print(item)
print('--------------------------------------------------------------------------')
# deep copy arr1 in arr4 using copy()
arr4 = arr3.copy()
# displaying the identity of arr4
print('\nArray 4 (Copy of Array 3) (ID:' +  str(id(arr4)) + '):')
for item in arr4:
    print(item)
print('--------------------------------------------------------------------------')
# making a change in arr3
arr3[2] = 8008
# displaying the arrays
print('\nAfter making a change in Array 3:')
print('\nArray 3:')
for item in arr3:
    print(item)
print('--------------------------------------------------------------------------')
print('\nArray 4 (Copy of Array 3):')
for item in arr4:
    print(item)