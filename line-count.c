#include <stdio.h>

int main() {
    FILE *file;
    char filename[100], ch;
    int lines = 0;

    printf("Enter the filename: ");
    scanf("%s", filename);

    file = fopen(filename, "r");

    if (file == NULL) {
        printf("Could not open file %s\n", filename);
        return 1;
    }

    while ((ch = fgetc(file)) != EOF) {
        if (ch == '\n') lines++;
    }

    fclose(file);
    printf("Number of lines: %d\n", lines);
    return 0;
}
