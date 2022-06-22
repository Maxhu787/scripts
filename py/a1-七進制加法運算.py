# 七進制加法運算

a='12345'
b='345'
c= ''

al=len(a); bl=len(b)
if al> bl :
    len=al
    b=b.rjust(len,'0')
else:
    len=bl
    a=a.rjust(len,'0')

carry=0

for i in range(len-1,-1,-1):
    s=int(a[i])+int(b[i])+carry
    m= (s%7)
    c=str(m)+c
    carry=(s//7)
    # print(c,'=',a[i],b[i],carry)
print(a,'+',b,'=',c)




