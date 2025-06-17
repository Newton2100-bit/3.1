#include <stdio.h>

int main(int argc , char * argv[]){
	int marks[5];
	marks[3] = 128;
	((short int *)marks)[6] = 2;
	printf("%d\n",marks[3]);
	return 0;
}
