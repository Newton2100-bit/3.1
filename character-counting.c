#include <stdio.h>

int main(void){
	long nc = 0;
	printf("Enter a character >");
	while(getchar() != EOF){
		++nc;
		printf("%i ",nc);
		printf("Enter a character again :");

	}
}
