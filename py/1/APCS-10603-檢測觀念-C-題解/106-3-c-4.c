#include <stdio.h>

int GCD (int a, int b) {
int r;
  r = a % b;
  if (r == 0)
    return  b ;
  return  GCD(b,r) ;
}

void main(){
    printf("%d",GCD(56,24));
}
