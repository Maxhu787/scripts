#include <stdio.h>
int F (int n) {
  if (n < 4){
    printf ("%d ", n );
    return n;
  }
  else{
    printf ("%d ", n );
    return n + F(n-3);
  }
}

void main(){
    printf("\nSum=%d ",F(14));
}
