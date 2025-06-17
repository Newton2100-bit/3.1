#include <stdio.h>
int main(int argc, char ** argv){ 
	int marks[] = {23,45,56,67,78,89,23,12}; 
	int * ptr; 
	ptr = marks; 
	for(int i=0;i<8;++i) 
		printf("%d\n",marks[i]);
	return 0;
}
