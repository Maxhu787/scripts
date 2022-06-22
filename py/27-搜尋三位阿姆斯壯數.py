# 搜尋三位阿姆斯壯數(水仙花數)
# http://gg.gg/py-armstrong ( 列出所有阿姆斯壯數 )

import time;  # 引入time 套件
#--------------------------------------------------------------
# 暴力法

t0 = time.time()

for a in range(0,10):
    for b in range(0,10):
        for c in range( 0,10):
            res=a**3+b**3+c**3
            dignum=int(str(a)+str(b)+str(c))
            if (res == dignum and res>10**2) :
                print(res)

t1 = time.time()
print("費時:",t1-t0) ; print("\n\n")
# -------------------------------------------------------------
# 避開相同數字 
t0 = time.time()

for a in range( 0,10):
    for b in range( a,10):
        for c in range( b,10):
            print(a,b,c)
            res=a**3+b**3+c**3
            dignum= str(a)+str(b)+str(c)
            if  ''.join(sorted(list(str(res)))) == dignum:
                print(''.join(sorted(list(str(res)))), dignum,res)
                
t1 = time.time()
print("費時:",t1-t0) ; print("\n\n")
# --------------------------------------------------------------

