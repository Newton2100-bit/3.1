#include <stdio.h>

int main() {
    char str[100];
    FILE *file;
    
    printf("Enter a string: ");
    scanf("%s", str);
    
    file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Could not open file for writing\n");
        return 1;
    }
    
    fprintf(file, "%s", str);
    fclose(file);
    
    printf("String written to output.txt\n");
    return 0;
}
