
#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    int len, i;
    printf("Enter a string: ");
    fgets(str, 100, stdin);

    len = strlen(str);
    printf("Reversed string: ");
    for (i = len - 1; i >= 0; i--) {
        putchar(str[i]);
    }
    return 0;
}
