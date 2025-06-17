#include <stdio.h>
int main(void){
	int guess;
	printf("Eneter your guess value >");
	while((scanf("%d",&guess) != EOF)){
		if(guess == 42){
			printf("..........Good guess Congraculation.\n");
			break;
		}
		else if(guess < 42){
			printf("The guess is a bit low guess again >");
		}
		else{ 
			printf("Too high guess agian >");
		}
	}
}
