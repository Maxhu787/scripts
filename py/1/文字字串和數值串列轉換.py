# n=int(input()) # 輸入單一整數資料
# data=input()   # 輸入一行連續資料
data='1 10 100 1000 10000' 
print(data)      # 輸入一行 文字字串

# 1. 文字字串轉乘數值串列
datalist01=list(map(int,data.split()))
print(datalist01)

# 2. 文字字串轉成文字串列
datalist02=data.split(' ') 
print(datalist02)

dataA='1 2 3 4 5'
datalist03=list(dataA) # 每個字元分開
print(datalist03)

# 3. 數值串列轉成文字字串 (字串右邊有空白)
n=len(datalist01)
for i in range(n):
    print(datalist01[i],end=' ')
print()

# 4. 文字串列轉成文字字串 (字串右邊有空白)
n=len(datalist02)
for i in range(n):
    print(str(datalist01[i]),end=' ')
print()

# 5. 輸出字串有時會要求前後沒有空白
strline=''
n=len(datalist02)
for i in range(n):
    strline=strline+' '+str(datalist02[i])
print(strline)           # (字串左邊有空白)
print(strline.strip())   # 去除前後空白


    
    




'''
s=0
for i in range(5):
    s=s+int(list[i])
print(s)



strline=''
for i in range(5):
    strline=strline+str(list[i])+' '
print(strline)

strline=''
for i in range(5):
    strline=strline+' '+str(list[i])
print(strline)

print(strline.strip())  

strline=''
for i in range(5):
    if i ==0 :
        strline=strline+str(list[i])
    else :
        strline=strline+' '+str(list[i])
print(strline)

strline=''
for i in range(5):
    strline=strline+(i>0)*' '+str(list[i])
print(strline)

strline=''
listA=[1,2,3,4,5]
print(listA)
for i in range(5):
    strline=strline+' '+str( listA[i])
print(strline.strip()) 
    
'''

    

''' 串列型態的綜合運算

v=[int(x) for x in list] #將輸入的字串變整數
print(v)

s=0
for i in range(5):
    s=s+v[i]

print(s)
'''
