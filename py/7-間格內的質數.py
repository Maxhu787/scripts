#顯示間隔內的所有質數

low = 20
up = 40

# low = int(input("輸入開始範圍: "))
# up = int(input("輸入結束範圍: "))

print(low,"至",up," 間隔內的所有質數:")

for n in range(low, up + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
            print(n, end=' ')
