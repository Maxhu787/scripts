# 檢查輸入數字是否為質數
num = 41

# 質數數字大於1
if num > 1:
   # 檢查因素
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"不是質數")
           print(i,"x",num//i,"是",num)
           break
   else:
       print(num,"是質數")
       
# 如果輸入數小於或等於1，就不是質數
else:
   print(num,"不是質數")

        
