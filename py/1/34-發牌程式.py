# 發牌
import random
 
flower='♥♠♦♣'  # 發色:花色的ASCII代碼分別為"3,4,5,6"但不一定相容
                 # 此處用 UTF-8中文內碼: 9829、9824、9830、9827 
nstr='A23456789TJQK'    # 數值大小
c=[]                    # 定義一個空的 c 串列 (List)
for i in range(0,52):
   c.append(i)          # 新產生的亂數用 append 附加在list的後面
# print(c)
 
for i in range(0,51):                  # 產生52個亂數
    s=random.randint(0,51)             # 指定亂數值 在 0~51
    temp=c[i];c[i]=c[s];c[s]=temp
# print(c)
 
for i in range(0,52):
    f=c[i]//13; n=c[i]%13   # 用商數決定花色，用餘數決定數值
    print(flower[f:f+1]+nstr[n],end=' ')
    if ( i%13==12):
        print()             # 要分4組列印，當印13個以後要下跳一行
