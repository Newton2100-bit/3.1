#include <stdio.h>
int main(void){
	int n,array[100],c,d,t;
	printf("Enter nuber of elements\n");
	scanf("%d",&n);
	printf("Enter %d integers \n",n);

	for(c=0;c<n;++c) scanf("%d",&array[c]);

	for(c=1;c <= n - 1 ; ++c){
		d = c;

		while(d > 0 && array[d-1] > array[d] ){
			t = array[d];
			array[d] = array[d-1];
			array[d-1] = t;
			d--;
		}
	}
	printf("Sorted list in ascending order : \n [ ");

	for(c = 0 ; c <= n - 1 ; ++c) printf("%d ,",array[c]);
	printf("]\n");
	return 0;
}
