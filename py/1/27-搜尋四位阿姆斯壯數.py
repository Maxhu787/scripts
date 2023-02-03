# 搜尋四位阿姆斯壯數(水仙花數)
# http://gg.gg/py-armstrong ( 列出所有阿姆斯壯數 )

import time;  # 引入time 套件
#--------------------------------------------------------------
# 暴力法

t0 = time.time()


for a in range( 0,10):
    for b in range( 0,10):
        for c in range( 0,10):
            for d in range( 0,10):
                res=a**4+b**4+c**4+d**4
                if res== int(str(a)+str(b)+str(c)+str(d)):
                    print( res)

t1 = time.time()
print("費時:",t0) ; print("\n\n")
# -------------------------------------------------------------
# 避開相同組合的數字 
t0 = time.time()

for a in range( 0,10):
    for b in range( a,10):
        for c in range( b,10):
            for d in range( c,10):
                res=a**4+b**4+c**4+d**4
                if  ''.join(sorted(list(str(res)))) == str(a)+str(b)+str(c)+str(d):
                    print(''.join(sorted(list(str(res)))), str(a)+str(b)+str(c)+str(d),res)
                
t1 = time.time()
print("費時:",t0) ; print("\n\n")
# --------------------------------------------------------------

