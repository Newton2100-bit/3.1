#include <stdio.h> 
// Function prototypes 
int recursive_binary_search(int arr[], int left, int right, int key); 
// Main function 
int main() { 
  int arr[] = {1, 3, 5, 7, 9, 11, 13, 15}; 
  int n = sizeof(arr) / sizeof(arr[0]); 
  int key; 
  printf("Enter the number to search: "); 
  scanf("%d", &key); 
  // Recursive Binary Search 
  int binary_recur_result = recursive_binary_search(arr, 0, n - 1, key); 
  printf("Recursive Binary Search: Element %s found\n", 
         (binary_recur_result == -1) ? "not" : "is"); 
  return 0; 
} 
//Recursive Binary Search 
int recursive_binary_search(int arr[], int left, int right, int key) { 
  if (left > right) 
    return -1; 
  int mid = left + (right - left) / 2; 
  if (arr[mid] == key) 
    return mid; 
  if (arr[mid] < key) 
    return recursive_binary_search(arr, mid + 1, right, key); 
  return recursive_binary_search(arr, left, mid - 1, key); 
}

