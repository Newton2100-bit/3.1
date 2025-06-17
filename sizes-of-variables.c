#include <stdio.h>
int main(void){
	char grade = 'A';
	int total = 98;
	float cost = 45.67f;
	double cost2 = 567.787;
	
	double mark1 = 67.56;
	float mark2 = 67.56f;

	printf("Size of float is %d.\n",sizeof(mark2));
	printf("The size of double is %d.\n",sizeof(mark1));

	printf("The size of int is %d bytes\n",sizeof(total));
	printf("The size of char is %d byte\n",sizeof(grade));
	printf("The size of float is %d bytes\n",sizeof(cost));
	printf("The size of double is %d bytes\n",sizeof(cost2));
	return 0;
}
