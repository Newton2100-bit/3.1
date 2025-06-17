#include <stdio.h>
#include <assert.h>

int divide(int a, int b) {
    assert(b != 0); // Ensure that b is not zero to avoid division by zero
    return a / b;
}

int main() {
    int numerator = 10;
    int denominator = 0;

    int result = divide(numerator, denominator);

    printf("Result: %d\n", result);

    return 0;
}

