#1050305-25

def  Mystery(x):
    if  ( x <= 1 ):
        return x
    else:
        return  ( Mystery(x-2) +  Mystery(x-1) )

#main
Mystery(9)
for i in range(10):
    print("Mystery(%d)之回傳值為%d"  %(i,Mystery(i)))




