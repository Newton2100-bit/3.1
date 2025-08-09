#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <error.h>

#define PERMS 0644
char *progname;


int main(argc, argv)
int argc;
char *argv[100];

{
  int f1, f2, n;
  char buf[BUFSIZ];

  progname = argv[0];
  if(argc != 3){
    fprintf(stderr,"Usage: %s from to.\n", progname);
  }


  if((f1 = open(argv[1], 0)) ==  -1){
    fprintf(stderr,"Can't open %s.\n",argv[1]);
  }


  if((f2 = creat(argv[2], PERMS)) == -1){
    fprintf(stderr,"Can't create %s.\n",argv[2]);
  }


  while((n = read(f1, buf , n)) > 0){
    if(write(f2, buf, n) != n){
      fprintf(stderr,"Write error.\n");
    }
  }
  return 0;
}
