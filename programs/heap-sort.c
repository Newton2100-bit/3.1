#include <stdio.h>

// Function declarations
void create(int heap[]);
void down_adjust(int heap[], int i);

int main() {
    int heap[30], n, i, last, temp;

    // Input the number of elements
    printf("Enter number of elements: ");
    scanf("%d", &n);

    // Input the elements (1-based indexing)
    printf("Enter elements: ");
    for (i = 1; i <= n; i++) {
        scanf("%d", &heap[i]);
    }

    heap[0] = n;  // Store size at index 0

    // Step 1: Build max heap
    create(heap);

    // Step 2: Perform Heap Sort
    while (heap[0] > 1) {
        last = heap[0];

        // Swap root with last element
        temp = heap[1];
        heap[1] = heap[last];
        heap[last] = temp;

        heap[0]--;  // Shrink heap
        down_adjust(heap, 1);  // Re-heapify
    }

    // Step 3: Print sorted array
    printf("Array after sorting:\n");
    for (i = 1; i <= n; i++) {
        printf("%d ", heap[i]);
    }
    printf("\n");

    return 0;
}

// Builds a max heap using bottom-up method
void create(int heap[]) {
    int n = heap[0];
    for (int i = n / 2; i >= 1; i--) {
        down_adjust(heap, i);
    }
}

// Maintains max-heap property from index i downwards
void down_adjust(int heap[], int i) {
    int j, temp, n = heap[0], flag = 1;

    while (2 * i <= n && flag) {
        j = 2 * i;

        // Pick larger child
        if (j + 1 <= n && heap[j + 1] > heap[j])
            j = j + 1;

        if (heap[i] >= heap[j])
            flag = 0;
        else {
            // Swap parent and larger child
            temp = heap[i];
            heap[i] = heap[j];
            heap[j] = temp;

            i = j;  // Move down
        }
    }
}

