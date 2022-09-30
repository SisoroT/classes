#include <stdio.h>
#include <stdlib.h>

int main() {
  FILE *fptr;
  int N;

  // run the program 200 times
  int i;
  for (i = 0; i < 200; i++) {

    // perform steps on each of the 3 processes
    int proc;
    for (proc = 1; proc <= 3; proc++) {

      // open file to read
      fptr = fopen("read.txt", "r");
      // read number from file
      fscanf(fptr, "%d", &N);
      // print number and the process id
      printf("N = %d, Process ID = P%d\n", N, proc);
      // close file
      fclose(fptr);

      // increment number by 1
      N++;
      // open file to write
      fptr = fopen("read.txt", "w");
      // write incremented number to file
      fprintf(fptr, "%d", N);
      // close file
      fclose(fptr);
    }
    // blank line between each 3 processes
    printf("\n");
  }
  return 0;
}
