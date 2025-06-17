#include <stdio.h>
#include <time.h>

int main() {
	time_t unix_time = time(NULL); // Get current Unix timestamp
	struct tm *time_info = localtime(&unix_time); // Convert to local time representation
	char date_str[50];

	strftime(date_str, sizeof(date_str), "%Y-%m-%d %H:%M:%S", time_info); // Format date
	printf("Formatted Date: %s\n", date_str);

	return 0;
}
