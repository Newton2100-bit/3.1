#include <stdio.h>

int main() {
    int a = 10;
    int b = 0;
    int result = a / b; // Division by zero - this will cause a runtime error
    printf("Result: %d\n", result);
    return 0;
}
