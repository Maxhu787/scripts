#1050305-2
# 本題找出最大的數，在陣列最後一次出現的位置(第幾個)

def f(a,n):
    index=0
    for i in range(1,n):
        print(i,a[i],index,a[index])   # 追蹤 最後一次 index = 7
        if (a[i] >= a[index]):
            index=i
    return index

#main
a=[1,3,9,2,5,8,4,9,6,7]
print("回傳值為",f(a,10))


