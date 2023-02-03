n=407 ; s=0
# 方法1: 用字串處理，依序取字元
for i in range(3):
      s=s+int(str(n)[i:i+1])**3      
if s==n: print(n ,"是阿姆斯壯數")

# 方法2: 用數值處理，依序取數值位元
##     2-1 :  依餘數順序取數值位元

d,s=0,0
for i in range(1,4):
    d=(n%(10**i)-n%(10**(i-1)))//(10**(i-1)); # print(d)
    s=s+d**3 ; # print(s)
if s==n: print(n ,"是阿姆斯壯數")

##     2-2 :  依商數順序取數值位元
m,s=0,0
for i in range(0,3):
    m=(n//(10**i))-(((n//(10**i))//10)*10); # print(m)
    s=s+m**3 ; # print(s)
if s==n: print(n ,"是阿姆斯壯數")
