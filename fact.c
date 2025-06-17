#include <stdio.h>
#include <stdlib.h>

int main(int argc , char * argv[]){
	int i , n , fact = 1;
	printf("\nEnter a number :");
	scanf("%d",&n);
	for(i=1;i <= n ; ++i) 
		fact *=i;
	printf("The factor of %d is %d \n",n,fact);
	return 0;
}
