#include <stdio.h>
int main()
{
	FILE *fpt;
	fpt=fopen("/dev/pts/3","w");
	fprintf(fpt,"Hello terminal.");
	fclose(fpt);
	return 0;
}
