#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: copy [sourcefile] [destfile]\n");
        exit(0);
    }

    FILE *src, *dest;
    if ((src = fopen(argv[1], "r")) == NULL) {
        printf("Unable to open %s for reading\n", argv[1]);
        exit(0);
    }

    if ((dest = fopen(argv[2], "w")) == NULL) {
        printf("Unable to open %s for writing\n", argv[2]);
        fclose(src);
        exit(0);
    }

    char c;
    while ((c = fgetc(src)) != EOF) {
        fputc(c, dest);
    }

    fclose(src);
    fclose(dest);
    return 0;
}
