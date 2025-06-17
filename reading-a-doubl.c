#include<stdio.h>
int main(void){
int num = printf("Enter a number : ");
double number;
int total = scanf("%lf",&number);
printf("The number you printed is %f\n",number);
char text[50];
sprintf(text,"The printf = %d and scanf = %d \n",num,total);
printf("%s\n",text);
return 0;
}
