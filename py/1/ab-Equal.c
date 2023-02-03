#include<stdio.h>
/* https://msdn.microsoft.com/zh-tw/library/cc953fe1.aspx */
int main() {
   float a,b;
   printf("Please input a number: \n");
   scanf("%f",&a);
   printf("%f\n",a);
   b=a+1;
   printf("%f\n",b);
   if ( a==b)
     printf("a=b");
}
