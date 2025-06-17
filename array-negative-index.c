#include <stdio.h>
#include <stdlib.h>
int main(int argc , char * argv[]){
	int marks[] = { 10,20,30,40,50,60,70,80,90};
	int age = (marks + 1)[-1];
	for(int i = 0; i < (sizeof(marks)/sizeof(int));++i)
		printf("%d \t",marks[i]);
	printf("\nValue of negative array index %d\n",age);
	return 0;
}
