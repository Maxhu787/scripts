# x=True ;  y=False
# print("%2d %2d" % (x,y))


# d=[11, 12, 13, 14, 15, 3]
d=[11, 12, 13, 14, 25, 20]
# d=[23, 15, 18, 20, 11, 12]
# d=[18, 17, 19, 24, 15, 16]

val=d[5]
allBig=True

for i in range(0,5):
    if ( d[i]> val):
        allBig=True;   # 刪除 這二行
    else:              # 刪除 這二行
        allBig= False
    # print(d[i],allBig)
if (allBig == True):
    print("%d is the smallest.\n" % val)
else:
    print("%d is not the smallest.\n"% val)





