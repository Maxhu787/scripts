# 陣列反轉 (飆程式網 #1011 )
# n=int(input())
# ipline= ()
n=5
ipline="2 3 12 4 5"

ipline=' '+ipline+' '

numlist=[]
strlen=len(ipline)
c=0 ;k=0 ; l=0;  r=0

for i in range(strlen):
    if ipline[i]==' ':
        l=k; r=i
        k=r
        c=c+1
        if c>1 :
            numlist.append(int(ipline[l+1:r]))
numlist.reverse()
c=len(numlist)
r=''
for i in range(c):
    if i<c-1 :
        r=r+str(numlist[i])+' '
    else:
        r=r+str(numlist[i])
print(r)
