#The difference between a shallow copy and a deep copy is that in a shallow copy, we create a new collection and populate it with REFERENCES to child objects from the original. This means that any changes made to the copy also reflects on the original, and vice versa. Whereas in a deep copy, we create a new collection and recursively creates copies of the objects from the original. This means that the original and the copy are independent of each other and any changes made on either do not reflect on the other.

#Shallow copy
# importing the module
from numpy import array
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
print('\nCopy of Array 1 (ID:' +  str(id(arr2)) + '):')
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
print('\nArray 2:')
for item in arr2:
    print(item)


