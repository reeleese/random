#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define SZ 21  // Cannot be more than 99

// Just add the numbers in the array
static int sum1(int *array, int size) {
  int i, sum=0;
  for (i=0; i<size; ++i) {
    sum += array[i];
  }
  return sum;
}

// Add the squares of the numbers
static int sum2(int *array, int size) {
  int i, sum=0;
  for (i=0; i<size; ++i) {
    sum += array[i] * array[i];
  }
  return sum;
}

// Array elements are the sum of the digits (range 0 to 99 only)
int main(int argc, char *argv[]) {
  int data[SZ];
  int i;
  for (i = 0; i < SZ; i++) data[i] = i % 10 + i / 10;
  int total1 = sum1(data, SZ);
  int total2 = sum2(data, SZ);
  printf("Sum1=%d Sum2=%d\n", total1, total2);
  // Check md5sum: 3fd78a160fb6e984506602b1e36ffb82
  return 0;
}
