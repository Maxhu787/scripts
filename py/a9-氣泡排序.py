# 氣泡排序
import random          # 導入套件
s=[]                   # 宣告串列

a = [5,2,1,9,6]        # 先以list做示範，設定串列 a 有五個元素
print(sorted(a))       #  a 由小到大排序，用 List 的排序函數
a.append(7)            # 串列用 append 附加 7
print(sorted(a))       # 再列印一次
print()
# ------------------------------------------------
for i in range(1,7):
    s.append(random.randint(1,100))  # 產生6 個 1~100 亂數
    print(s[i-1],end=' ')            # 印出亂數    
print('\n')

print('1. 印出未排序亂數串列')
print(s)
print()

print('2. 印出排序亂數串列')
print(sorted(s))                     # 有內建函數 sorted 排序
print()

print('3. 印出未排序陣列')
for i in range(0,6):
    print(s[i],end=" ")              # 依陣列位置依序印出
print('\n')

# ------------------------------------------------
for i in range(0,6):               # 氣泡排序
    for j in range(i+1,6):
        if (s[j] < s[i]):          # 由小到大
            temp=s[j]              # 交換
            s[j]=s[i]
            s[i]=temp
    print('第',i,'次排序:')
    for k in range(0,6):
        print(s[k],end=' ')
    print()  
print()

print('4. 印出由小到大排序陣列')           
for i in range(0,6):             # 印出陣列
    print(s[i],end=" ")
print()    

# ------------------------------------------------
for i in range(0,6):             # 氣泡排序
    for j in range(i+1,6):
        if (s[j] > s[i]):          # 由大到小
            s[i],s[j]=s[j],s[i]    # 交換
print()

print('5. 印出由大到小排序陣列')  
for i in range(0,6):             # 印出陣列
    print(s[i],end=" ") 

