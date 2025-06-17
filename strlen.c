#include <stdio.h>
#include <string.h>

int main(int argc,char * argv[]){
	char name[] = {"Newton irungu"};
	int length = strlen(name);
	printf("The length of %s is %d.\n",name,length);
	return 0;
}
