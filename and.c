#include <stdio.h>
#include <unistd.h>

int main(int argc , char * argv[]){

	int num1 = 90, num2 = 67;
	int num3 = num1 && num2;
	printf("Our value of %d && %d is : %d\n",num1,num2,num3);
	int val1 = 0, val2 = 2;
	int val4 = val1 && val2;
	printf("the value of %d && %d is :%d\n",val1,val2,val4);

	return 0;
}

