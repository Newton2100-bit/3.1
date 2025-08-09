#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

int main(void){

  int fd = open("nonExistingFile.txt",O_RDONLY);
  if(fd == -1){
    perror("open failed\n");
    return 1;
  }
  close(fd);
}
