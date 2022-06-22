alist=[1,2,3,4,]

def runvar( alist=alist):
    print(alist)
    alist.append(5)

runvar()
print(alist)
