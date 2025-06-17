#include <stdio.h>

int main(int argc , char ** argv){
FILE * fpt = fopen("/dev/pts/1","w");
fprintf(fpt,"Hello user hope your terminal is good \n");
fclose(fpt);
return 0;
}
