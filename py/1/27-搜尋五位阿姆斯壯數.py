# 搜尋五位阿姆斯壯數(水仙花數)
# http://gg.gg/py-armstrong ( 列出所有阿姆斯壯數 )

import time;  # 引入time 套件
#--------------------------------------------------------------
# 暴力法

t0 = time.time()


for a in range( 0,10):
    for b in range( 0,10):
        for c in range( 0,10):
            for d in range( 0,10):
                for e in range( 0,10):
                    res=a**5+b**5+c**5+d**5+e**5
                    dignum=int(str(a)+str(b)+str(c)+str(d)+str(e))
                    if (res == dignum)  and ( res > 10**4):
                        print( res)

t1 = time.time()
print("費時:",t1-t0) ; print("\n\n")
# -------------------------------------------------------------
# 避開相同組合的數字 
t0 = time.time()

for a in range( 0,10):
    for b in range( a,10):
        for c in range( b,10):
            for d in range( c,10):
                for e in range(d,10):
                    # print(a,b,c,d,e)
                    res=a**5+b**5+c**5+d**5+e**5
                    dignum= str(a)+str(b)+str(c)+str(d)+str(e)
                    if  ''.join(sorted(list(str(res)))) == dignum:
                        print(''.join(sorted(list(str(res)))), dignum,res)
                
t1 = time.time()
print("費時:",t1-t0) ; print("\n\n")
# --------------------------------------------------------------

