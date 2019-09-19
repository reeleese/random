#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define SZ 43

typedef struct MMM {
  int total1;
  int total2;
} mmm_t;

static mmm_t *mmm3(int *array, int size) {
  static mmm_t mmm;
  // TBD
}

int main(int argc, char *argv[]) {
  int data[SZ];
  int i;
  for (i = 0; i < SZ; i++) data[i] = i % 10 + i / 10;
  mmm_t *mmm = mmm3(data, SZ);
  printf("Sum1=%d Sum2=%d\n", mmm->total1, mmm->total2);
  // Check md5sum: f4396288060d404d6c204084310521d3
  return 0;
}
