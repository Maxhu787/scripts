# 字串轉陣列 再轉字串
# n=int(input()) # 系統單筆資料取法
# ipline= ()     # 系統整行資料取法

n=5
ipline="1 10 100 1000 10000"

print(n)
newlist = ipline.split(' ')       # 字串轉陣列函數 
print(newlist)
# (你的程式在這裡)
newstr = ' '.join(newlist)        # 陣列轉字串函數
print(newstr)                     # 送出字串 
