#include <stdio.h>
int main(void){
	int array[4] = {23,45,56,78};
	int *ptr1,*ptr2;
	ptr1=array;
	ptr2=&array[2];
	int total = ptr1-ptr2;
	printf("The total size of ints is %d\n",total);

	printf("The value of array is %p\n",array);
	printf("The value of &array[2] is %p\n",&array[2]);
	return 0;
}
