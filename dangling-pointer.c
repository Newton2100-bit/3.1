#include <stdio.h>
#include <stdlib.h>

int main(void){
printf("\033[4;1;36mWelcome to our program we gonna be lookig and dangling pointers.\033[0m\n");
  int *ptr = malloc(sizeof(int));

  if(ptr != NULL){
    printf("\033[034mSuccessful memory allocation.\n");
  }else {
    perror("\033[91mAn error occured\033[0m]");
    exit(0);
  }

  *ptr = 7070;
  printf("we have stored the value %d in our dynamiccaly allocated memory.\n",*ptr);
  printf("The memory add ress is %p .\n",ptr);

  free(ptr);
  printf("After freeing the memory location is %p.\n",ptr);

  ptr = NULL;
  printf("Our final pointer value is %p.\033[0m\n",ptr);
}

