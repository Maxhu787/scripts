#include <stdio.h>

void F() {
  int X[10] = {0};
  printf( "請輸入: \n" );
  printf( "0 1 2 3 4 5 6 7 8 9\n" );
  for (int i=0; i<10; i=i+1) {
    scanf("%d", &X[(i+2)%10]);
  }
  for (int i=0; i<10; i=i+1) {
    printf("%d ",  X[i]);
  }

}



int main () {
  F();
}
