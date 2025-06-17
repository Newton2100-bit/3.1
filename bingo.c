#include <stdio.h>
#include <string.h>

int main(int argc , char * argv[]){
	char text[80];
	while(1){
		scanf("%s",text);
		if(strcmp(text,"sum=5")==0) 
			printf("Bingo!\n");
		else if(strcmp(text,"sum=12")==0)
			break;
	}
	return 0;
}
