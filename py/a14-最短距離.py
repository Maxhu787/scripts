# 最短路徑
list1= \
[(  0,  10,   1,1000,1000), \
(1000   ,0,1000,  20,1000), \
(1000,1000,   0,   2   ,5), \
(1000,1000,1000,   0,   2), \
(1000,1000,1000,1000,   0)]

d=0
small=1000

def perm(a,k=0):

    global d,small,alist
    if k == len(a):
        # print(a,end='') # 可以列出排列
        d=0 
        if a[0] ==0 :
            for i in range(0,4):
                d=d+list1[a[i]][a[i+1]]                
                if a[i+1]== 4:
                    # print(d)
                    break
            if small > d:   # 如果新的 d 小於 small 
                p=' 0'
                small =d    # 記住最短距離
                alist=a[0:a.index(4)+1]
                # print(small,d)
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i] ,a[k]
            perm(a, k+1)
            a[k], a[i] = a[i], a[k]

perm([0,1,2,3,4])
print('最短路徑=',alist)
print('最短距離=',small)




        

