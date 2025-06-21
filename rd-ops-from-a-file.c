#include <stdio.h>

int main() {
    FILE *file;
    int num, sum = 0;
    
    file = fopen("numbers.txt", "r");
    if (file == NULL) {
        printf("Could not open file numbers.txt\n");
        return 1;
    }
    
    while (fscanf(file, "%d", &num) != EOF) {
        sum += num;
    }
    
    fclose(file);
    printf("Sum of integers in the file: %d\n", sum);
    return 0;
}
