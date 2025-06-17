#include <stdio.h>

int main(int argc , char * argv[]){
	int x , sum = 0;
	while(1){
//		printf("#? ");
		scanf("%d",&x);
		if ( x==0 ) 
			break;
		sum = sum + x;
		printf(" sum=%d\n",sum);
	}
	return 0;
}
