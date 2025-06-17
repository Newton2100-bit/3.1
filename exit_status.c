#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <sys/wait.h>
#include <sys/types.h>

int main(void){
pid_t pid1,pid2,pid3;
pid1=fork();
if(pid1==0){
printf("Child : %d : I'm the child executing\n",getpid());
printf("As the child i am sleeping 2 seconds before exiting with status 12 \n");
sleep(2);
exit(12);
}
else if(pid1 > 0){
int status;
pid2 = wait(&status);
if(WIFEXITED(status)){
printf("parent process executing now after my chiuld terminated \n");
printf("The child exit status was %d \n",WEXITSTATUS(status));
}
}
if(pid1 == -1){
perror("fork failed");
exit(2);
}
return 0;
}

