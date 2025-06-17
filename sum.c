#include <stdio.h>
int sum(int num1 ,int num2);

int main(void){
	int num1 , num2;
	printf("Enter num1 :");
	scanf("%d",&num1);
	printf("and num2 :");
	scanf("%d",&num2);
	printf("The sum of your numbers is %d\n",sum(num1,num2));

	printf("************DONE******************\n");
}

int sum(num1,num2) int num1,num2;{

	return (num1 + num2);
}
