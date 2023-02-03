# 8-6-2-1 顯示間隔內的所有質數
a = 50
b = 100

lstprime=[]
# a = int(input("輸入開始範圍: "))
# b = int(input("輸入結束範圍: "))
 
print(a,"至",b," 間隔內的所有質數:")

def prime(a,b):
    for n in range(a, b + 1):
        if n > 1:
            for i in range(2,n):
                if (n % i) == 0:
                    break                 # 如果  (n % i) == 0 跳出迴圈
            else:
                    lstprime.append(n)


prime(50,100)
print(lstprime)
      
