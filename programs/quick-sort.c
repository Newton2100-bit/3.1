#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 10


void quiksort(int*,int,int);
void swap(int*,int,int);
int partition(int*,int,int);

int main(void){
	int array[MAX_SIZE],i,n;
	printf("enter number of elements\n");

	int number;
	scanf("%d",&number);

	printf("Enter your values\n");
	for(n = 0; n < 5; n++)
		scanf("%d",&array[n]);


	quiksort(array,0,n-1);

	printf("\nOutput : ");

	for(i = 0;i<number;i++)
		printf("%d ",array[i]);

	printf("\n");

	return 0;
}

void swap(int array[],int one,int two)
{
	int temp = array[one];
	array[one] = array[two];
	array[two] = temp;
}

int partition(int array[],int left,int right)
{
	int pivot = array[right];
	int leftpointer = left-1;
	int rightpointer = right;
	for(;;){
		while(array[++leftpointer] > pivot){}

		while(rightpointer > 0 && array[--rightpointer] < pivot) {}

		if(leftpointer >= rightpointer) break;
		else swap(array,leftpointer,rightpointer);
	}
	swap(array,leftpointer,right);
	return leftpointer;
}




void quiksort(int array[],int left,int right)
{
	if(left < right) {
		int partitionpoint = partition(array,left,right);
		quiksort(array,left,partitionpoint);
		quiksort(array,partitionpoint+1,right);
	}
}


