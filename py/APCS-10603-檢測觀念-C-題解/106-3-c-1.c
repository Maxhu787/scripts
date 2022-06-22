#include <stdio.h>

int A[8]={0, 2, 4, 6, 8, 10, 12, 14};
int Search (int x) {
  int high = 7;
  int low = 0;
  while (high > low) {
    int mid = (high + low)/2;
    if (A[mid] <= x) {
      low = mid + 1;
    }
    else {
      high = mid;
    }
  }
  return A[high];
}

void main(void){
  printf("%d",Search(16));
}
