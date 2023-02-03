a=[1,2,3,4,5,6]
print(a)
n=len(a)
for  i in range((n-2)+1):
    hold   =   a[i]
    a[i]     =   a[i+1]
    a[i+1] =   hold

print(a)
