# 因為本程式執行的時間較長，所以也順便計算本程式的執行時間

import time;  # 引入time 套件

 
t1 = time.time()
print( "開始時間:", t1, "\n")

# 查特定字元的ASCII值

c = 'A'
print( c + "的ASCII值=",ord(c),hex(ord(c)))

c = 'a'
print( c + "的ASCII值=",ord(c),hex(ord(c)))

for i in range( 32, 127):
    print(i,"=",chr(i),end=" | ")

print('\n')

for i in range( 32, 127):
    print( i,"=",chr(i),end=" | ") 
 
t2 = time.time()
print ("\n結束時間:" , t2)
print ("執行時間:" , t2-t1 ,"秒")
