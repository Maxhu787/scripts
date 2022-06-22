x = 10          # 全域變數
y = 20          # 全域變數
lista=[]        # 全域變數

def showvar():
    global y,lista
    listb=[5,4,3,2,1]    
    lista=listb     # 區域變數 
    y = 10          # 區域變數
    lista.append(6)
    print('showvar=',lista)
   
def localvar():
    y = 30          # y 區域變數 
    z = 40          # z 區域變數
    print('x=',x)   # x 區域變數
    print("localvar 區域 y =",y)
    print("localvar 全域 lista=",lista,'\n')
   
print('main x=',x)  # 全域變數
showvar()
localvar()
print('main y=',y)
print('main lista=',lista)


