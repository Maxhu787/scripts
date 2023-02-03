#include <stdio.h>
int c;
void F(int x) {         // 遞迴 ????
  int i;

  for (i=0; i<x; i=i+1)
    printf("* ");
    c=c+1;
  if (x>1) {
    F(x/2);
    F(x/2);
  }
}

void A1(int n) {
  F(n/5);
  F(4*n/5);
}

void A2(int n) {
  F(2*n/5);
  F(3*n/5);
}

void main(void)
{
  c=0;
  A1(5);
  printf("c=%d",c);
}
