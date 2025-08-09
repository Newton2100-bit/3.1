#include <stdio.h>
#include <stdarg.h>

// ANSI color codes
#define RED "\033[91m"
#define RESET "\033[0m"

// Function to print red error messages to stderr
void eprint_red(const char* format, ...) {
    va_list args;
    
    // Print red color code to stderr
    fprintf(stderr, "%s", RED);
    
    // Print the formatted message to stderr
    va_start(args, format);
    vfprintf(stderr, format, args);
    va_end(args);
    
    // Print reset code to stderr
    fprintf(stderr, "%s", RESET);
}

// Alternative version that automatically adds newline
void eprint_red_ln(const char* format, ...) {
    va_list args;
    
    fprintf(stderr, "%s", RED);
    
    va_start(args, format);
    vfprintf(stderr, format, args);
    va_end(args);
    
    fprintf(stderr, "%s\n", RESET);
}

// Simple version for just strings (no formatting)
void eprint_red_simple(const char* message) {
    fprintf(stderr, "%s%s%s", RED, message, RESET);
}

// More comprehensive error printing with different colors
void print_colored(FILE* stream, const char* color, const char* format, ...) {
    va_list args;
    
    fprintf(stream, "%s", color);
    va_start(args, format);
    vfprintf(stream, format, args);
    va_end(args);
    fprintf(stream, "%s", RESET);
}

// Macro for easy red error printing
#define ERROR_RED(format, ...) print_colored(stderr, RED, format, ##__VA_ARGS__)

int main() {
    // Usage examples
    eprint_red("This is a red error message");
    eprint_red_ln("\nThis is a red error message with newline");
    eprint_red_simple("Simple red message\n");
    
    // With formatting
    int error_code = 404;
    eprint_red_ln("Error %d: File not found", error_code);
    
    // Using the macro
    ERROR_RED("Macro error: %s\n", "Something went wrong");
    
    return 0;
}
