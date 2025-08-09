#include <stdio.h>
#include <unistd.h>

#define PROGRESS_WIDTH 50
#define TOTAL_STEPS 100
#define SLEEP_TIME 50000 // in microseconds

void draw_progress(int percent) {
    int filled = (percent * PROGRESS_WIDTH) / 100;
    printf("\r[");  // Carriage return to overwrite the line
    for (int i = 0; i < PROGRESS_WIDTH; ++i) {
        if (i < filled)
            printf("█");
        else
            printf(" ");
    }
    printf("] %3d%%", percent);
    fflush(stdout);
}

int main() {
    printf("\033[1;32mInstalling package...\033[0m\n"); // Green colored message

    for (int i = 0; i <= TOTAL_STEPS; ++i) {
        draw_progress(i);
        usleep(SLEEP_TIME);
    }

    printf("\n\033[1;34mDone!\033[0m\n"); // Blue colored message
    return 0;
}

