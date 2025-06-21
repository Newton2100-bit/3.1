#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: toupper [filename]\n");
        exit(0);
    }

    FILE *fpt;
    if ((fpt = fopen(argv[1], "r")) == NULL) {
        printf("Unable to open %s for reading\n", argv[1]);
        exit(0);
    }

    char c;
    while ((c = fgetc(fpt)) != EOF) {
        putchar(toupper(c));
    }

    fclose(fpt);
    return 0;
}
