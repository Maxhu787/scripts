# 印月曆

# 輸入年
y=2020

# 判斷是否為閏年
leap=0
if y % 4 == 0 :
    leap=1
if y % 100==0:
    leap=0
if y % 400==0:
    leap=1

# 輸入月
m=4

md=[0,31,28,31,30,31,30,31,31,30,31,30,31]
if leap == 1:
    md=[0,31,29,31,30,31,30,31,31,30,31,30,31]
blk24=24*' ' # 24 個空白要印在每月 1 日的前面 (好用的運算)

sumday=0                            
for i in range(0,m):    
    sumday=sumday+md[i]         # 算在1月1日到輸入月份1日前共幾天
    
# print(sumday)    
w=y+y/4-y/100+y/400+sumday
week=int(w % 7)                 # 算輸入月份的 1 日星期幾 ?
print('',y,'年 ',m, '月')

print(' Sun Mon Tue Wed Thu Fri Sat')
print(blk24[0:week*4],end='')    # 先印空白
for i in range(1,md[m]+1):
    print("%4d" %i,end='')      # 跟著印
    if (( week+i) %7 ==0 ):     # 到星期六下跳一行
        print()


