#include <stdio.h>

int main() {
    FILE *file = fopen("example.txt", "rb");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }
    
    char buffer[100];
    size_t bytesRead = fread(buffer, sizeof(char), 99, file);
    buffer[bytesRead] = '\0';  // Null-terminate if reading text
    
    printf("Read %zu bytes: %s\n", bytesRead, buffer);
    
    fclose(file);
    return 0;
}
