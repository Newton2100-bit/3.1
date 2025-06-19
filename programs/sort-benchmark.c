#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#define MAX_ELEMENT_IN_ARRAY 1000000001

// Comparison function for qsort
int cmpfunc(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

// Generate random array
int* generate_random_array(int n) {
    srand(time(NULL));
    int *a = malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i)
        a[i] = rand() % MAX_ELEMENT_IN_ARRAY;
    return a;
}

// Copy array
int* copy_array(int *a, int n) {
    int *copy = malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i)
        copy[i] = a[i];
    return copy;
}

// Insertion Sort (Ascending)
void insertion_sort_asc(int *a, int start, int end) {
    for (int i = start + 1; i <= end; ++i) {
        int key = a[i];
        int j = i - 1;
        while (j >= start && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;
    }
}

// Merge utility for Merge Sort
void merge(int *a, int start, int end, int mid) {
    int i = start, j = mid + 1, k = 0;
    int *aux = malloc(sizeof(int) * (end - start + 1));

    while (i <= mid && j <= end)
        aux[k++] = (a[i] <= a[j]) ? a[i++] : a[j++];

    while (i <= mid) aux[k++] = a[i++];
    while (j <= end) aux[k++] = a[j++];

    for (i = start, k = 0; i <= end; ++i, ++k)
        a[i] = aux[k];

    free(aux);
}

// Recursive Merge Sort
void merge_sort_recursive(int *a, int start, int end) {
    if (start < end) {
        int mid = start + (end - start) / 2;
        merge_sort_recursive(a, start, mid);
        merge_sort_recursive(a, mid + 1, end);
        merge(a, start, end, mid);
    }
}

// Merge Sort wrapper
void merge_sort(int *a, int n) {
    merge_sort_recursive(a, 0, n - 1);
}

// Hybrid Merge-Insertion Sort
void hybrid_sort(int *a, int start, int end, int k) {
    if (start < end) {
        int size = end - start + 1;
        if (size <= k) {
            insertion_sort_asc(a, start, end);
            return;
        }
        int mid = start + (end - start) / 2;
        hybrid_sort(a, start, mid, k);
        hybrid_sort(a, mid + 1, end, k);
        merge(a, start, end, mid);
    }
}

// Performance comparison
void test_sorting_runtimes(int size, int num_of_times) {
    double insertion_sort_time = 0, merge_sort_time = 0;
    double hybrid_time = 0, qsort_time = 0;

    for (int t = 0; t < num_of_times; ++t) {
        int *a = generate_random_array(size);
        int *b = copy_array(a, size);
        int *c = copy_array(a, size);
        int *d = copy_array(a, size);
        int *e = copy_array(a, size);

        clock_t start, end;

        start = clock();
        insertion_sort_asc(b, 0, size - 1);
        end = clock();
        insertion_sort_time += (double)(end - start) / CLOCKS_PER_SEC;

        start = clock();
        merge_sort(c, size);
        end = clock();
        merge_sort_time += (double)(end - start) / CLOCKS_PER_SEC;

        start = clock();
        hybrid_sort(d, 0, size - 1, 40);  // k = 40 threshold
        end = clock();
        hybrid_time += (double)(end - start) / CLOCKS_PER_SEC;

        start = clock();
        qsort(e, size, sizeof(int), cmpfunc);
        end = clock();
        qsort_time += (double)(end - start) / CLOCKS_PER_SEC;

        free(a); free(b); free(c); free(d); free(e);
    }

    insertion_sort_time /= num_of_times;
    merge_sort_time /= num_of_times;
    hybrid_time /= num_of_times;
    qsort_time /= num_of_times;

    printf("\nAverage time to sort %d elements over %d run(s):\n", size, num_of_times);
    printf("1. Insertion Sort:         %f sec\n", insertion_sort_time);
    printf("2. Merge Sort:             %f sec\n", merge_sort_time);
    printf("3. Hybrid Merge-Insertion: %f sec\n", hybrid_time);
    printf("4. qsort (C Library):      %f sec\n", qsort_time);
}

// Main
int main() {
    int t;
    printf("Enter number of test cases: ");
    scanf("%d", &t);

    while (t--) {
        int size, runs;
        printf("\nEnter array size and number of runs: ");
        scanf("%d %d", &size, &runs);
        test_sorting_runtimes(size, runs);
    }

    return 0;
}

