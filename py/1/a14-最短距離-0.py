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
        d=0 
        print (a)
        if a[0] ==0 :
            for i in range(0,4):
                print(a[i],a[i+1],list1[a[i]][a[i+1]])
                d=d+list1[a[i]][a[i+1]]
                if a[i+1]== 4:
                    break
            if small > d:
                p=' 0'
                small =d
                print('4=',a.index(4))
                alist=a[0:a.index(4)+1]
            print('d,min =',d,small)      
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i] ,a[k]
            perm(a, k+1)
            a[k], a[i] = a[i], a[k]

for i in range(5):
    for j in range(5):
        print(list1[i][j],end=' ')
    print()

perm([0,1,2,3,4])
print('最短路徑=',alist)
print('最短距離=',small)




        

