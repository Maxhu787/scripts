#include <stdio.h>

void main(){
  int A[2][3] = {0, 1, 2, 3, 4, 5};
  // http://epaper.gotop.com.tw/pdf/AEL013400.pdf 二維陣列
  // 0,1,2
  // 3,4,5

  int rowsum = 0;
  int M=2;
  int N=3;
  for (int i=0; i<M; i=i+1) {
    for (int j=0; j<N; j=j+1) {
      rowsum = rowsum + A[i][j];
    }
    printf("The sum of row %d is %d.\n", i, rowsum);
  }
}

