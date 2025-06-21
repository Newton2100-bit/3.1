
#include <stdio.h>
#include <ctype.h>

int main() {
    FILE *fptr;
    char filename[100], c;
    int word_count = 0, in_word = 0;

    printf("Enter the filename: ");
    scanf("%s", filename);

    fptr = fopen(filename, "r");

    if (fptr == NULL) {
        printf("Cannot open file \n");
        return 1;
    }

    while ((c = fgetc(fptr)) != EOF) {
        if (isspace(c)) {
            in_word = 0;
        } else if (!in_word) {
            in_word = 1;
            word_count++;
        }
    }

    fclose(fptr);

    printf("Word count: %d\n", word_count);

    return 0;
}

#include <ctype.h>

int main() {
    FILE *fptr;
    char filename[100], c;
    int word_count = 0, in_word = 0;

    printf("Enter the filename: ");
    scanf("%s", filename);

    fptr = fopen(filename, "r");

    if (fptr == NULL) {
        printf("Cannot open file \n");
        return 1;
    }

    while ((c = fgetc(fptr)) != EOF) {
        if (isspace(c)) {
            in_word = 0;
        } else if (!in_word) {
            in_word = 1;
            word_count++;
        }
    }

    fclose(fptr);

    printf("Word count: %d\n", word_count);

    return 0;
}

