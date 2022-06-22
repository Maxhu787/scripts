# 是否為阿姆斯壯數
sum = 0 ; num = 370 ; temp = num

while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp = temp // 10 # 也可寫成 temp //= 10

if num == sum:
   print(num,"是阿姆斯壯數")
else:
   print(num,"不是阿姆斯壯數")
