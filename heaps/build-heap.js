// To heapify a subtree rooted with node i which is
// an index in arr[]. N is size of heap
function heapify(arr, n, i) {
    let largest = i; // Initialize largest as root
    let l = 2 * i + 1; // left = 2*i + 1
    let r = 2 * i + 2; // right = 2*i + 2

    // If left child is larger than root
    if (l < n && arr[l] > arr[largest])
        largest = l;

    // If right child is larger than largest so far
    if (r < n && arr[r] > arr[largest])
        largest = r;

    // If largest is not root
    if (largest !== i) {
        [arr[i], arr[largest]] = [arr[largest], arr[i]];

        // Recursively heapify the affected sub-tree
        heapify(arr, n, largest);
    }
}

// Function to build a Max-Heap from the given array
function buildHeap(arr, n) {
    // Index of last non-leaf node
    let startIdx = Math.floor(n / 2) - 1;

    // Perform reverse level order traversal
    // from last non-leaf node and heapify
    // each node
    for (let i = startIdx; i >= 0; i--) {
        heapify(arr, n, i);
    }
}

// A utility function to print the array
// representation of Heap
function printHeap(arr, n) {
    console.log("Array representation of Heap is:");

    for (let i = 0; i < n; ++i)
        process.stdout.write(arr[i] + " ");
    console.log("\n");
}

// Driver Code
const arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17];

const n = arr.length;

// Function call
buildHeap(arr, n);
printHeap(arr, n);

// Final Heap:
//              17
//            /    \
//          15      13
//         /  \     / \
//        9     6  5   10
//       / \   / \
//      4   8 3   1
