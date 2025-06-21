#include <stdio.h>
#include <ctype.h>

int main() {
    char str[100];
    int i, count = 0;
    printf("Enter a string: ");
    fgets(str, 100, stdin);

    for (i = 0; str[i] != '\0'; i++) {
        if (tolower(str[i]) == 'a' || tolower(str[i]) == 'e' || tolower(str[i]) == 'i' || 
            tolower(str[i]) == 'o' || tolower(str[i]) == 'u') {
            count++;
        }
    }

    printf("Number of vowels: %d\n", count);
    return 0;
}
