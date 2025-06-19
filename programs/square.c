#include <stdio.h>
int square(int);
int main(void){
int num;
scanf("%d",&num);
printf("The square of %d is %d \n",num,square(num));
return 0;
}

int square(num) int num;{
return num * num;
}
