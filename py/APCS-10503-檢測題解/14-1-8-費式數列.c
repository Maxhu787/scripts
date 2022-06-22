#include <stdio.h>

int main(void)
{
    int a=0;
    int b=1;
    int i,temp,N;
    N=10;
    for (i=2;i<=N;i=i+1)
    {
        temp =b;
        b=a+b;
        a=temp;
        printf("%d\n",b);
    }
}
