#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(void){
pid_t pid1 = fork();
pid_t pid2 = fork();

for(int i = 0 ; i < 4 ; ++i)
printf("%d : Newton \n",getpid());

return 0;
}


