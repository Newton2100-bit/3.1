#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void get_current_time(char *buffer, size_t size) {
    time_t rawtime;
    struct tm *timeinfo;

    time(&rawtime);
    timeinfo = localtime(&rawtime);

    strftime(buffer, size, "%Y-%m-%d %H:%M:%S", timeinfo);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: logentry [logfile]\n");
        exit(0);
    }

    FILE *fpt;
    if ((fpt = fopen(argv[1], "a")) == NULL) {
        printf("Unable to open %s for appending\n", argv[1]);
        exit(0);
    }

    char timestamp[20];
    char message[1000];

    get_current_time(timestamp, sizeof(timestamp));
    printf("Enter log message: ");
    fgets(message, sizeof(message), stdin);

    fprintf(fpt, "[%s] %s", timestamp, message);

    fclose(fpt);
    return 0;
}
