#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#define STACK_SIZE 100

typedef struct {
	size_t disks;
	char source;
	char auxiliary;
	char destination;
} Frame;
Frame stack[STACK_SIZE];

int top = -1;

void push(int disks, char source, char auxiliary, char destination);
void hanoi_iterative(int n,char source,char auxiliary,char destination);
Frame pop(void);

int main(void) {
	int n;
	printf("Enter number of disks: ");
	scanf("%d", &n);
	hanoi_iterative(n, 'A', 'B', 'C');
	return 0;
}

void hanoi_iterative(n,source,auxiliary,destination)
	int n;
	char source,auxiliary,destination;
{
	push(n, source, auxiliary, destination);

	while (top >= 0) {
		Frame current = pop();

		if (current.disks == 1) printf("Move disk from %c to %c\n", current.source, current.destination);
		else {

			push(current.disks - 1, current.auxiliary, current.source, current.destination);  
			push(1, current.source, current.auxiliary, current.destination);                  
			push(current.disks - 1, current.source, current.destination, current.auxiliary);  
		}
	}
}


Frame pop(void) {
	if (top < 0) assert(0);
	return stack[top--];
}


void push(int disks, char source, char auxiliary, char destination) {
	if (top >= STACK_SIZE - 1) assert(0);
	stack[++top] = (Frame){disks, source, auxiliary, destination};
}



