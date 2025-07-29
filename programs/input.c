#include <stdio.h>
#define MAX_SIZE 20
int main(void){
	int number;
	int array[MAX_SIZE];
	printf("Enter total values you wish to calculate\n");
	scanf("%d",&number);
	printf("Enter your values now\n");
	for(int i = 0; i < number; ++i)
		scanf("%d",&array[i]);
	printf("The sum is :");
	int sum = 0;
	for(int i = 0;i < number;++i)
		sum +=array[i];
	printf("The total of your values is %d\n",sum);
	return 0;
}


