#include <stdio.h>
int main(int argc, char * arvgv[]){
/*	int val1 = 40;
	float val2 = *(float*)&val1;
	printf("The float value is %f \n",val2);

	float f = 7.0;
	printf("value of float is %2.4f\n",f);
	short int i = *(short int *)&f;
	char ch = *(char *)&f;
	printf("The value of %f is %c\n",f,ch);
	printf("Final value of float is %f \n",f);


	int val3 = 67;
	char val4 = *(char *)&val3;
	printf("The value of %d is %c\n",val3,val4);

	char val5 =  'c';
	int val6 = val5;
	
	printf("The value of c is %d\n",val6);
*/
	short int x = 45;
	double d = *(double *)&x;
	printf("The value of %d is %lf\n",x,d);

	return 0;
}
