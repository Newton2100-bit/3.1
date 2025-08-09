#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *fp = fopen("access.log", "r");
    if (!fp) {
        perror("File open failed");
        return 1;
    }
    char line[1024];
    int count_200 = 0, count_404 = 0, count_500 = 0;
    while (fgets(line, sizeof(line), fp)) {
        if (strstr(line, " 200 ")) count_200++;
        else if (strstr(line, " 404 ")) count_404++;
        else if (strstr(line, " 500 ")) count_500++;
    }
    fclose(fp);
    return 0;
}
