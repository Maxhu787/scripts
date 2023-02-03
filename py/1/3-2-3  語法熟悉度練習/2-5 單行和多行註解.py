# 九九乘法表
	
''' ( 這是多行註解 )
print(i*j, end=”)
是在print( , end='')函數的第二個參數，加上了end=''
'''

for i in range(1,10):
    for j in range (1,10):  
        if i*j < 10 :
            print ('', i*j, end=' ') #不換行，跟著印
        else:       
            print (i*j , end=' ')    #不換行，跟著印
    print(end ='\n')                 #換行
