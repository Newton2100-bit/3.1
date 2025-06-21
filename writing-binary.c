#include <stdio.h>

int main() {
    FILE *file = fopen("numbers.bin", "wb");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }
    
    int numbers[] = {1, 2, 3, 4, 5};
    size_t count = sizeof(numbers) / sizeof(numbers[0]);
    
    size_t written = fwrite(numbers, sizeof(int), count, file);
    
    printf("Written %zu integers\n", written);
    
    fclose(file);
    return 0;
