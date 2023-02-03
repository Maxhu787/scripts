#include <stdio.h>

void main(){
  int i;
  int A[5]={1,2,3,4,5 };
  int p =  A[0];
  int q =  A[0];
  int n=5;
  for (int i=1; i<n; i=i+1) {
    if (A[i] > p)
      p = A[i];
      if (A[i] < q)
        q = A[i];
  }
  printf ("%d  %d", q,p);
}
