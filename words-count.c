
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: wordcount [filename]\n");
        exit(0);
    }

    FILE *fpt;
    if ((fpt = fopen(argv[1], "r")) == NULL) {
        printf("Unable to open %s for reading\n", argv[1]);
        exit(0);
    }

    int words = 0;
    int in_word = 0;
    char c;

    while ((c = fgetc(fpt)) != EOF) {
        if (isspace(c)) {
            if (in_word) {
                words++;
                in_word = 0;
            }
        } else {
            in_word = 1;
        }
    }

    if (in_word) words++;  // Count the last word if it exists

    fclose(fpt);

    printf("Number of words: %d\n", words);
    return 0;
}
