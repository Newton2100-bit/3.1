#include <stdio.h>
#include <string.h>
int main(void){
char * reverse(char[] string);
char name[] = "Newton Irungu Mwaura";
int length = strlen(name);
printf("The length of your name is %d",length);
return 0;
}

char * reverse(char[] string){
char string2[];
strcpy(string2,string);
char temp;
int length = strlen(string),count=length-1;
for(int i = 0 ;i < length/2 ; ++i){
strcpy(temp,string2[0];
strcpy(string2[0],string2[count]);
strcpy(string2[count],temp);
count--;
}
}
