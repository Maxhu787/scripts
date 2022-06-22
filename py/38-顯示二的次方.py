# 函數顯示數的2次方
n = 6

# 用lambda 運算式來定義函式
r = list(map(lambda x: 2 ** x, range(n))) 

print("總共算到 2 的:",n-1,"次方")
for i in range(n):    #不註明起始值，會從零開始 range(0,16)
   print("2 的",i,"次方=",r[i])

