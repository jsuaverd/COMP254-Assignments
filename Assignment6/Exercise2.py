# Define a function that adds two numbers
def add(x, y):
    return x + y

# Define two lists of numbers
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

# Use map() to add corresponding elements of the two lists using the add function
result = list(map(add, list1, list2))

# Display the result
print("The element-wise sum of the two lists is:", result)
