#include<stdio.h>

int foo (int i) {
  if (i <= 5) {
    printf ("foo: %d\n", i);
    }
  else {
    printf ("foo->i: %d\n", i,"-> bar: %d\n", i-10);
    bar(i - 10);
    }
  }

int  bar (int i) {
  if (i <= 10) {
    printf ("bar: %d\n", i);
    }
  else {
    printf ("bar->i: %d\n",i,"-> bar: %d\n", i-5);
    foo(i - 5);
    }
  }

void main() {
  foo(15106);
  /* bar(3091);  */
  /* foo(6693);  */

  /* foo(106); */
  /* bar(91);  */
  /* foo(93);  */
  }
