#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void){
char * args[] = {"./exec",NULL};
char * argc[] = {"newton","irungu",NULL};
execvp(args[0],argc);
printf("Ending >>>>>");
return 0;
}
