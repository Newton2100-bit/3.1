
#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fptr;
    char filename[100];
    long file_size;
    char *buffer;

    printf("Enter the filename: ");
    scanf("%s", filename);

    fptr = fopen(filename, "r");

    if (fptr == NULL) {
        printf("Cannot open file \n");
        return 1;
    }

    fseek(fptr, 0, SEEK_END);
    file_size = ftell(fptr);
    fseek(fptr, 0, SEEK_SET);

    buffer = (char*)malloc(file_size + 1);
    fread(buffer, 1, file_size, fptr);
    buffer[file_size] = '\0';

    fclose(fptr);

    printf("Reversed content:\n");
    for (long i = file_size - 1; i >= 0; i--) {
        printf("%c", buffer[i]);
    }
    printf("\n");

    free(buffer);
    return 0;
}
