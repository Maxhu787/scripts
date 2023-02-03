#include <stdio.h>

int n = 0;
void K (int b) {
  n = n + 1;
  if (b % 4)
  K(b+1);
}

void G (int m) {
  for (int i=0; i<m; i=i+1) {
    K(i);
  }
}


int main () {
  G(100);
  printf("%d",n);
}
