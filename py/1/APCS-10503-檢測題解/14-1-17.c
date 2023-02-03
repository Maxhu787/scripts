#include<stdio.h>

#define TRUE 1
#define FALSE 0

int main(void) {
    int d[6], val, allBig;
    for (int i=1; i<=5; i=i+1) {
      scanf ("%d", &d[i]);
    }

    scanf ("%d", &val);
    allBig = TRUE;

    for (int i=1; i<=5; i=i+1) {
      if (d[i] > val) {
        allBig = TRUE;
      }
      else {
        allBig = FALSE;
      }
    }

    if (allBig == TRUE) {
      printf ("%d is the smallest.\n", val);
    }
    else {
      printf ("%d is not the smallest.\n", val);
    }
return 0;
}
