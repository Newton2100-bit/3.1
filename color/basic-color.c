#include <stdio.h>

int main() {
    printf("\033[1;31mHello, World!\033[0m\n");
    printf("\033[32mThis is green text\033[0m\n");
    printf("\033[44mBlue background\033[0m\n");
    printf("\033[1;33;41mBold yellow on red\033[0m\n");
    
    return 0;
}
