#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main(void){
  FILE * fptr = NULL;
  int fd = open("data.txt",O_RDWR | O_CREAT ,0644);
  char text[200] = "This was a reap on how to use the write() function and let me tell you brother\nC isn't a language to be played with\nJust be aware don't say you weren't told\n";
  int writing = write(fd,text,sizeof text);

  if(writing == 0){
    perror("An error ocurred brothers\n");
  }

  printf("if you are seing this then the write was successful\n");


}
