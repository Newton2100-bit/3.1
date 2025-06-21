#include <stdio.h>

int main() {
    FILE *fptr;
    char filename[100], str[100];

    printf("Enter the filename: ");
    scanf("%s", filename);

    fptr = fopen(filename, "a");

    if (fptr == NULL) {
        printf("Cannot open file \n");
        return 1;
    }

    printf("Enter a string to append to the file: ");
    getchar(); // consume newline left by scanf
    fgets(str, 100, stdin);

    fprintf(fptr, "%s", str);
    fclose(fptr);

    printf("Content appended to the file.\n");

    return 0;
}
