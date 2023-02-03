# 數字的階乘
num = 7
fact = 1

# 檢查數字是否為負數，正數或零
if num < 0:
   print("負數不存在因數")
elif num == 0:
   print("0的因數為1")
else:
   for i in range(1,num + 1):
       fact = fact*i
   print(num,"!=",fact) 

