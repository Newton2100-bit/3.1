class MaxHeap:
    """
    Complete Max Heap implementation with all essential operations
    """
    
    def __init__(self, arr=None):
        """Initialize heap from array or empty"""
        if arr:
            self.heap = arr.copy()
            self.build_heap()
        else:
            self.heap = []
    
    def parent(self, i):
        """Get parent index of node i"""
        return (i - 1) // 2
    
    def left_child(self, i):
        """Get left child index of node i"""
        return 2 * i + 1
    
    def right_child(self, i):
        """Get right child index of node i"""
        return 2 * i + 2
    
    def heapify_down(self, i):
        """
        Heapify downward from index i (max-heapify)
        Time: O(log n), Space: O(1)
        """
        size = len(self.heap)
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        # Compare with left child
        if left < size and self.heap[left] > self.heap[largest]:
            largest = left
        
        # Compare with right child
        if right < size and self.heap[right] > self.heap[largest]:
            largest = right
        
        # If largest is not the current node, swap and continue
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            print(f"  Swapped {self.heap[largest]} and {self.heap[i]} at indices {largest} and {i}")
            self.heapify_down(largest)  # Recursive call
    
    def heapify_up(self, i):
        """
        Heapify upward from index i (for insertion)
        Time: O(log n), Space: O(1)
        """
        while i > 0:
            parent_idx = self.parent(i)
            if self.heap[i] <= self.heap[parent_idx]:
                break
            
            # Swap with parent
            self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i]
            print(f"  Bubbled up: swapped {self.heap[parent_idx]} and {self.heap[i]}")
            i = parent_idx
    
    def build_heap(self):
        """
        Build max heap from arbitrary array using Floyd's algorithm
        Time: O(n), Space: O(1)
        """
        print("Building heap using bottom-up heapify...")
        size = len(self.heap)
        
        # Start from last non-leaf node and heapify each
        for i in range(size // 2 - 1, -1, -1):
            print(f"\nHeapifying at index {i} (value: {self.heap[i]})")
            self.heapify_down(i)
            print(f"Heap after heapifying index {i}: {self.heap}")
    
    def insert(self, value):
        """
        Insert new value into heap
        Time: O(log n), Space: O(1)
        """
        print(f"\nInserting {value}")
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
        print(f"Heap after insertion: {self.heap}")
    
    def extract_max(self):
        """
        Remove and return maximum element
        Time: O(log n), Space: O(1)
        """
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Store max value
        max_val = self.heap[0]
        
        # Move last element to root and heapify down
        self.heap[0] = self.heap.pop()
        print(f"Extracted {max_val}, moved {self.heap[0]} to root")
        self.heapify_down(0)
        print(f"Heap after extraction: {self.heap}")
        
        return max_val
    
    def peek(self):
        """Return maximum element without removing"""
        return self.heap[0] if self.heap else None
    
    def size(self):
        """Return heap size"""
        return len(self.heap)
    
    def is_empty(self):
        """Check if heap is empty"""
        return len(self.heap) == 0
    
    def display_tree(self):
        """Display heap as tree structure"""
        if not self.heap:
            print("Empty heap")
            return
        
        def print_level(level_start, level_size, max_width):
            if level_start >= len(self.heap):
                return
            
            level_end = min(level_start + level_size, len(self.heap))
            spacing = max_width // (level_size + 1)
            
            line = " " * spacing
            for i in range(level_start, level_end):
                line += f"{self.heap[i]:2d}" + " " * (spacing - 1)
            print(line)
        
        levels = 0
        temp = len(self.heap)
        while temp > 0:
            temp //= 2
            levels += 1
        
        max_width = 2 ** levels * 4
        level_start = 0
        level_size = 1
        
        print("\nTree representation:")
        for _ in range(levels):
            print_level(level_start, level_size, max_width)
            level_start += level_size
            level_size *= 2
            max_width //= 2
    
    def __str__(self):
        return f"MaxHeap: {self.heap}"


def heap_sort(arr):
    """
    Sort array using heap sort algorithm
    Time: O(n log n), Space: O(1)
    """
    print(f"\n{'='*50}")
    print("HEAP SORT DEMONSTRATION")
    print(f"{'='*50}")
    
    print(f"Original array: {arr}")
    
    # Build max heap
    heap = MaxHeap(arr)
    print(f"Max heap built: {heap.heap}")
    
    # Extract elements in descending order
    sorted_arr = []
    original_size = heap.size()
    
    print(f"\nExtracting elements:")
    for i in range(original_size):
        max_element = heap.extract_max()
        sorted_arr.append(max_element)
        print(f"Step {i+1}: Extracted {max_element}")
    
    # Reverse for ascending order
    sorted_arr.reverse()
    print(f"\nFinal sorted array: {sorted_arr}")
    return sorted_arr


def demonstrate_heap_operations():
    """Comprehensive demonstration of heap operations"""
    
    print("="*60)
    print("COMPREHENSIVE HEAP IMPLEMENTATION DEMONSTRATION")
    print("="*60)
    
    # Example 1: Build heap from array
    print("\n1. BUILDING HEAP FROM ARRAY")
    print("-" * 30)
    arr = [1, 8, 6, 3, 4, 2, 5]
    print(f"Original array: {arr}")
    heap = MaxHeap(arr)
    heap.display_tree()
    
    # Example 2: Insert operations
    print(f"\n2. INSERTION OPERATIONS")
    print("-" * 30)
    heap.insert(10)
    heap.insert(15)
    heap.insert(12)
    heap.display_tree()
    
    # Example 3: Extract operations
    print(f"\n3. EXTRACTION OPERATIONS")
    print("-" * 30)
    print(f"Current heap: {heap}")
    
    max1 = heap.extract_max()
    print(f"Extracted: {max1}")
    
    max2 = heap.extract_max()
    print(f"Extracted: {max2}")
    
    heap.display_tree()
    
    # Example 4: Heap sort
    heap_sort([64, 34, 25, 12, 22, 11, 90])
    
    # Example 5: Performance comparison
    print(f"\n4. ALGORITHM COMPLEXITY ANALYSIS")
    print("-" * 40)
    print("Operation          Time        Space")
    print("-" * 40)
    print("Build Heap         O(n)        O(1)")
    print("Insert             O(log n)    O(1)")
    print("Extract Max        O(log n)    O(1)")
    print("Peek               O(1)        O(1)")
    print("Heapify            O(log n)    O(1)")
    print("Heap Sort          O(n log n)  O(1)")


# Additional utility functions for testing
def is_valid_max_heap(arr):
    """Check if array represents valid max heap"""
    n = len(arr)
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True


def compare_build_methods():
    """Compare different heap building approaches"""
    print(f"\n5. COMPARING HEAP BUILDING METHODS")
    print("-" * 40)
    
    arr = [4, 10, 3, 5, 1, 15, 9, 7, 6, 12]
    print(f"Original array: {arr}")
    
    # Method 1: Bottom-up (Floyd's algorithm)
    print(f"\nMethod 1: Bottom-up heapify (O(n))")
    heap1 = MaxHeap(arr.copy())
    print(f"Result: {heap1.heap}")
    print(f"Valid heap: {is_valid_max_heap(heap1.heap)}")
    
    # Method 2: Top-down insertion
    print(f"\nMethod 2: Top-down insertion (O(n log n))")
    heap2 = MaxHeap()
    for val in arr:
        heap2.insert(val)
    print(f"Result: {heap2.heap}")
    print(f"Valid heap: {is_valid_max_heap(heap2.heap)}")


if __name__ == "__main__":
    # Run comprehensive demonstration
    demonstrate_heap_operations()
    compare_build_methods()
    
    print(f"\n{'='*60}")
    print("DEMONSTRATION COMPLETE!")
    print(f"{'='*60}")