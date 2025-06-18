#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc,char * args[]){
	printf("Hello sir newton this is exec executing \n");
	printf("This is because we hava your demo program being replaced\n");
	
	printf("Total arguments sent : %d",argc);
	for(int i=0; i<argc ; ++i)
		printf("%d : %s \n",i,args[i]);

	return 0;
}


