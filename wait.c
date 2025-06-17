#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char * argv[]){
	pid_t pid = fork();
	if( pid==0){
		printf("inside the child process %d \n",getpid());
		int num1,num2;
		printf("Enter two value to evaluate their sum \n");
		scanf("%d %d",&num1,&num2);
		printf("The sum of your two values is %d + %d = %d\n",num1,num2,num1+num2);
		printf("Child exiting\n\n\n");
		return 0;
	}
	if (pid> 0)
	{
		int status;
		pid_t pid1  = wait(&status);
		int num3,num4;
		printf("enter two numbers form two values \n");
		scanf("%d %d",&num3,&num4);
		printf("the total from your two values is %d + %d = %d\n",num3,num4,num3+num4);
		printf("parent exiting .....\n");
		return 0;
	}
}
