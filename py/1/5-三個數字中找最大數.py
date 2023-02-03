# 找到三個數字中 的最大數

n1 = 23 ; n2 = 8 ; n3 = 41

if (n1 >= n2) and (n1 >= n3):
   lar = n1
elif (n2 >= n1) and (n2 >= n3):
   lar = n2
else:
   lar = n3

print(n1,",",n2,"和",n3,"三數中最大數是",lar)
