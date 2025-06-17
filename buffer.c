#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc , char * argv[]){
	void print(int num);
	int num = 100;
	for( ; num>0 ; --num) print(num);
	return 0;
}

void print(int num){
	printf("i=%d\n ",num);
	sleep(1);
}

