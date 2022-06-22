#1050305-3
def f1(a, value, c):            # 循序搜尋
    i=0 ;  r_value = -1
    while ( i < 100 ):
        c += 1
        if (a[i] == value):
            r_value = i
            break
        i += 1
        # print (c,i, a[i])        # 搜尋到 value=100 , i=34 , n1=34 
    return  c

def  f2(a,value,c):              # 二分搜尋
    low=0 ; high=99
    while (low <= high):
        c += 1
        mid = (low + high)//2
        if  (a[mid] == value):
            r_value = mid
            break
        elif  (a[mid] < value):
            low = mid + 1
        else:
            high = mid -1
        # print (c,mid, a[mid])          # 搜尋到 value=100 , c=5 , n2=5  
    return  c

#main
a=[] ; value=100 ;n1=0 ; n2=0
for k in range(100):
    a.append(3*k+1)
    
# print(a)  # 陣列元素從 1 開始累加三: 1, 4, 7, 10, 13,
            # a[33]=100

n1=f1(a,value,n1)       # 循序搜尋 f1(a,100,0)
n2=f2(a,value,n2)       # 二分搜尋 f2(a,100,0)
print("n1=%d, n2=%d" %(n1,n2))

