#include <stdio.h>

int main() {
  // Write data
  FILE *writeFile = fopen("data.bin", "wb");
  if (writeFile == NULL) {
    perror("Error opening file for writing");
    return 1;
  }

  double values[] = {3.14, 2.71, 1.41, 1.73};
  fwrite(values, sizeof(double), 4, writeFile);
  fclose(writeFile);

  // Read data back
  FILE *readFile = fopen("data.bin", "rb");
  if (readFile == NULL) {
    perror("Error opening file for reading");
    return 1;
  }
  double readValues[4];
  size_t elementsRead = fread(readValues, sizeof(double), 4, readFile);

  printf("Read %zu elements:\n", elementsRead);
  for (int i = 0; i < elementsRead; i++) {
    printf("%.2f ", readValues[i]);
  }
  printf("\n");

  fclose(readFile);
  return 0;
}
double readValues[4];
size_t elementsRead = fread(readValues, sizeof(double), 4, readFile);

printf("Read %zu elements:\n", elementsRead);
for (int i = 0; i < elementsRead; i++) {
  printf("%.2f ", readValues[i]);
}
printf("\n");

fclose(readFile);
return 0;
}
