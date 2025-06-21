#include <stdio.h>
#include <string.h>

int main() {
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }
    
    char *text = "Hello, World!\n";
    size_t written = fwrite(text, sizeof char, strlen(text), file);
    
    printf("Written %zu characters\n", written);
    
    fclose(file);
    return 0;
}
