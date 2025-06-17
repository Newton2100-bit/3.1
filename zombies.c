#include <stdio.h>
#include <unistd.h>

int main(void){
pid_t pid;
int num1 , num2;
pid = fork();
printf("pid = %d :Enter two numbers :",getpid());
scanf("%d %d",&num1,&num2);
printf("\nThe total from pid = %d id %d + %d sum = %d \n",getpid(),num1,num2,num1+num2);
return 0;
}
