#include <stdlib.h>
#include <stdio.h>

void leak_memory() {
    int *ptr = malloc(sizeof(int) * 10); // Allocated but never freed
    ptr[10] = 42; // Invalid write (buffer overflow)
}

int main() {
    printf("Running Valgrind test...\n");
    leak_memory();
    return 0;
}
