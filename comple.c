#include <stdio.h>
#include <math.h>

int main()
{
    float a, b, c, discriminant, root1, root2, realPart, imaginaryPart;
    
    printf("Enter coefficients a, b, and c: ");
    scanf("%f %f %f", &a, &b, &c);
    
    // Check if 'a' is zero (not a quadratic equation)
    if (a == 0) {
        printf("Error: 'a' cannot be zero in a quadratic equation.\n");
        return 1;
    }
    
    discriminant = b * b - 4 * a * c;
    
    if (discriminant > 0) {
        // Two distinct real roots
        root1 = (-b + sqrt(discriminant)) / (2 * a);
        root2 = (-b - sqrt(discriminant)) / (2 * a);
        printf("Roots are real and distinct: %.2f and %.2f\n", root1, root2);
    }
    else if (discriminant == 0) {
        // One repeated real root
        root1 = root2 = -b / (2 * a);
        printf("Roots are real and equal: %.2f\n", root1);  // Fixed variable name
    }
    else {
        // Complex roots
        realPart = -b / (2 * a);
        imaginaryPart = sqrt(-discriminant) / (2 * a);
        printf("Roots are complex: %.2f + %.2fi and %.2f - %.2fi\n", 
               realPart, imaginaryPart, realPart, imaginaryPart);
    }
    
    return 0;
}
