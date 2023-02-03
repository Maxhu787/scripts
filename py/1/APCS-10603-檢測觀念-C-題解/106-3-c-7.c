#include <stdio.h>

int B (int n, int k) {
  if (k == 0 || k == n){
    printf ("base case\n");
    return 1;
  }
  return B(n-1,k-1) + B(n-1,k);
}


void main(){
  B(5,2);
}
