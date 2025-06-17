#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void){
	printf("This is the parent before forking\n");
	int value = 90;
	printf("The value before forking is %d\n",value);
	pid_t pid = fork();
	if(pid == 0) 
		printf("The child process in execution\n");

	if(pid == 0)
		value = 89;

	if(pid > 0)
		printf("Parent process in execution\n");

	printf("The value of num is %d \n",value);

	return 0;
}
/*
   int main (int argc , char * argv[]){
   pid_t pid;
   int value = 70;
   printf("original value of value is %d\n",value);
   printf("At the beginning i am the parent executing\n");
   int num = 7070;
   pid = vfork();
   if(pid==0){
   printf("Child process executing \n");
   num=num*4;
   value = 0;
   printf("my value of num is %d \n",num);
   }
   if (pid > 0){
   printf("I am excuting after the child has terminated \n");
   printf("the child left the valu eof num as %d \n",num);
   printf("final value of value is %d \n",value);

   }
   return 0;
   }
 */

