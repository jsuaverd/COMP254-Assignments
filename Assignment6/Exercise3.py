def find_peak_elements(arr):
    n = len(arr)
    peak_elements = []

    # Check if the list is empty or contains a single element
    if n == 0:
        return peak_elements
    elif n == 1:
        return [arr[0]]
    
    # Check for peak at the first position
    if arr[0] > arr[1]:
        peak_elements.append(arr[0])
    
    # Check for peak elements in the middle of the list
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            peak_elements.append(arr[i])
    
    # Check for peak at the last position
    if arr[n - 1] > arr[n - 2]:
        peak_elements.append(arr[n - 1])
    
    return peak_elements

# Example list
input_list = [8, 9, 10, 2, 5, 6]
peak_elements = find_peak_elements(input_list)
print("The peak elements are:", peak_elements)
