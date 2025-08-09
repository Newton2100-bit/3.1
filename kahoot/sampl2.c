#include <stdio.h>
#include <stdlib.h>
int main(void){
  int *ptr = malloc(4 * 100);
  ptr[0] = 10;
  // free(ptr);
  return 0;
}
