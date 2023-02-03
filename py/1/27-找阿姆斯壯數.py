# 1~1000 之間的阿姆斯壯數
sum = 0

for num in range(1,1000):
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** 3  # 也可寫成 sum += digit ** 3 
        temp = temp // 10       # 也可寫成 temp //= 10
    if num == sum:
        print(num,end=' ')
    sum=0    
        

