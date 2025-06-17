#include <stdio.h>

int main(void) {
	char name[10];
	/*printf("Enter your name kindly :");
	  scanf("%[^0-9]10s",name);
	  printf("Hello %s hope you are fine",name);*/
	char in[20];
	printf("Enter a test statement.\n");
	while(1){
		scanf("%s",in);
		printf("%s\t\t",in);
	}

	return 0;
}
