#include <stdio.h>

int main() {
    char filename[100];
    char ch;
    FILE *file;
    
    printf("Enter the file name: ");
    scanf("%s", filename);
    
    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Could not open file %s\n", filename);
        return 1;
    }
    
    while ((ch = fgetc(file)) != EOF) {
        putchar(ch);
    }
    
    fclose(file);
    return 0;
}
