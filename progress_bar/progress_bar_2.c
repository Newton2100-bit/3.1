#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

#define PROGRESS_WIDTH 50
#define TOTAL_STEPS 100
#define SLEEP_TIME 50000 // microseconds

int get_terminal_rows() {
    FILE *fp = popen("tput lines", "r");
    if (!fp) return 24; // Fallback
    int rows;
    fscanf(fp, "%d", &rows);
    pclose(fp);
    return rows;
}

void move_to_bottom(int rows) {
    printf("\033[%d;1H", rows); // Move cursor to last row, column 1
}

void draw_progress(int percent, int rows) {
    move_to_bottom(rows);
    int filled = (percent * PROGRESS_WIDTH) / 100;
    printf("\033[2K\r[");  // Clear line, carriage return
    for (int i = 0; i < PROGRESS_WIDTH; ++i)
        printf(i < filled ? "█" : " ");
    printf("] %3d%%", percent);
    fflush(stdout);
}

int main() {
    int rows = get_terminal_rows();
    printf("\033[?25l"); // Hide cursor
    printf("\033[1;32mInstalling package...\033[0m");

    for (int i = 0; i <= TOTAL_STEPS; ++i) {
        draw_progress(i, rows);
        usleep(SLEEP_TIME);
    }

    move_to_bottom(rows);
    printf("\n\033[1;34mDone!\033[0m\n");
    printf("\033[?25h"); // Show cursor again
    return 0;
}

