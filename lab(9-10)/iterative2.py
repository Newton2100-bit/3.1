import random

# Fixed data generation - creates a sorted list
data = list(range(2, 100, 2))  # Creates [2, 4, 6, 8, ..., 98]
print('The length of our list is', len(data))
print(data)

def binary_search(data, key):
    if len(data) == 0:
        return "Not found"
    
    middle = len(data) // 2  # Use integer division
    
    if key == data[middle]:
        return f'Found at index {middle}'
    elif key < data[middle]:
        # Search left half
        result = binary_search(data[:middle], key)
        if result.startswith("Found"):
            return result
        else:
            return result
    else:
        # Search right half
        result = binary_search(data[middle + 1:], key)
        if result.startswith("Found"):
            # Adjust index to account for the offset
            index = int(result.split()[-1]) + middle + 1
            return f'Found at index {index}'
        else:
            return result

# Alternative iterative implementation (more efficient)
def iterative_binary_search(data, key):
    low = 0
    high = len(data) - 1
    
    while low <= high:
        middle = (low + high) // 2
        
        if data[middle] == key:
            return f'Found at index {middle}'
        elif key < data[middle]:
            high = middle - 1
        else:
            low = middle + 1
    
    return "Not found"

found = int(input('Enter the value you want to search: '))
print("Recursive result:", binary_search(data, found))
print("Iterative result:", iterative_binary_search(data, found))
