#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void){
	int num1,num2,num3,num4;
	printf("Can you input your first 2 numbers \n");
	scanf ("%d %d",&num1,&num2);
	printf("The total was %d + %d = %d",num1,num2,num1+num2);
	printf("\nEnter the remaining two values \n");
	scanf("%d %d",&num3,&num4);
	printf("The total is %d + %d = %d\n",num3,num4,num3+num4);
	printf("The overrall total is %d + %d = %d\n",num1+num2,num3+num4,num1+num2+num3+num4);
	return 0;
}

