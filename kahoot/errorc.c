#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int fd = open("data.txt", O_RDONLY);
    if (fd == -1) {
        fprintf(stderr, "Error: %s\n", strerror(errno));
        return 1;
    }
    close(fd);
    return 0;
}
