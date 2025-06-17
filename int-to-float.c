#include <stdio.h>
int main(int argc , char * argv[]){
	int num = 37;
	printf("The value of num is %d\n",num);
	float fl = *((float*)&num);
	printf("The value of our float is %f\n",fl);
	printf("The value of num after conversion is %d\n",num);
	return 0;
}
