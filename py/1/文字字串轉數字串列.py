# ipline =input()
ipline='3 27 1586 93 688'
ipline=' '+ipline+' '

print(ipline)

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
print(numlist)
