# 背包問題

def perm(a,k=0):    
   global maxv,maxe    # 定義全域變數
   weight=0; val=0     # 重量和價值先設定為零
   if k == len(a):
      # print (a,end='')           # 這裡會印出所有排列組合
      for m in range(len(a)):
         # 計算串列中每一個的價值和重量
         pv=a[m];mw=int(w[pv-1]);mv=int(v[pv-1]) 
         
         weight=weight+mw       # 當選擇加入一項物品後計算重量
         if weight> 10 :        # 重量不能超過10
            break
         val=val+int(v[pv-1])      # 選取加入物品後的價值
         if val > maxv:
            maxv=val               # 記住這時候的最大價值
            maxe=a[0:m+1]          # 記住最大價值時候有哪些物件
      # print(' ',weight-mw,val,maxv) # 需要時這一行可以追蹤程式
      # input()
      weight=0; val=0           # 每一輪都要先把重量和價值清空
   else:
      for i in range(k, len(a)):   # 遞迴程式
         a[k], a[i] = a[i] ,a[k]
         perm(a, k+1)
         a[k], a[i] = a[i], a[k]
maxe=[] 
maxv=0
n=5
c=10
w=[2,2,6,5,4]
v=[6,3,5,4,6]
perm([1,2,3,4,5])
print('項目=',n,'項')
print('重量分別為:[2,2,6,5,4]')
print('價值分別為:[6,3,5,4,6]')
print('選取=',maxe,'項')
print('價值=',maxv)
