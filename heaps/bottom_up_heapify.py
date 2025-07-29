def heapify(arr, n, i):
    """Heapify subtree rooted at index i"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Compare with left child
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Compare with right child  
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not root, swap and continue
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_max_heap(arr):
    """Build max heap using bottom-up approach"""
    n = len(arr)
    
    # Start from last non-leaf node and heapify each
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    return arr

# Test the algorithm
if __name__ == "__main__":
    # Your example array
    arr = [1, 8, 6, 3, 4, 2, 5]
    print(f"Original: {arr}")
    
    build_max_heap(arr)
    print(f"Max Heap: {arr}")
    
    # Test with another array
    arr2 = [4, 10, 3, 5, 1, 15, 9, 7, 6, 12]
    print(f"\nOriginal: {arr2}")
    build_max_heap(arr2)
    print(f"Max Heap: {arr2}")
