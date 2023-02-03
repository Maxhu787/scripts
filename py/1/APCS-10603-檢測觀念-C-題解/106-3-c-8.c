#include <stdio.h>

int s = 1; // 全域變數
void add (int a) {
  int s = 6;
  for( ; a>=0; a=a-1) {
    printf("%d,", s);
    s++;
   printf("%d,", s);
  }
}


int main () {
  printf("%d,", s);
  add(s);
  printf("%d,", s);
  s = 9;
  printf("%d", s);
  return 0;
}

