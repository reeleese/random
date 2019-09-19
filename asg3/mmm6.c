#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define SZ 76

static void mmm6(int *array, int size, int *total1, int *total2) {
  *total1 = 0;
  *total2 = 0;

  int i;
  for (i=0; i<size; ++i) {
    *total1 += array[i];
    *total2 += array[i] * array[i];
  }
}

int main(int argc, char *argv[]) {
  int data[SZ];
  int i;
  int total1;
  int total2;
  for (i = 0; i < SZ; i++) data[i] = i % 10 + i / 10;
  mmm6(data, SZ, &total1, &total2);
  printf("Sum1=%d Sum2=%d\n", total1, total2);
  // Check md5sum: 659064637c2915657c5965d930aa33dd
  return 0;
}
