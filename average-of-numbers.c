#include <stdio.h>
Int int main(int argc, char *argv[])
{
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return EXIT_FAILURE;
    }

    FILE *file = fopen(argv[1], "rb");
    if (file == NULL) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    double sum = 0.0;
    int count = 0;
    double value;

    while (fread(&value, sizeof(double), 1, file) == 1) {
        sum += value;
        count++;
    }

    fclose(file);

    if (count == 0) {
        fprintf(stderr, "No numbers found in the file.\n");
        return EXIT_FAILURE;
    }

    double average = sum / count;
    printf("Average of numbers: %.2f\n", average);
  return EXIT_SUCCESS;
}
