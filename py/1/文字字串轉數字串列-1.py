# ipline =input()
ipline='3 27 1586 93 688'
ipline=' '+ipline+' '

numlist=[]
strlen=len(ipline)
print('len=',strlen)
for i in range(strlen):
    print(ipline[i],end='')
print()
c=0 ;k=0 ; l=0;  r=0

for i in range(strlen):    
    print(ipline[i],end='')
    if ipline[i]==' ':
        l=k; r=i
        print("c=",c,l,r,'\n')
        k=r
        c=c+1
        if c>1 :
            print(len(ipline[l+1:r]),ipline[l+1:r])
            print(int(ipline[l+1:r]))
            numlist.append(int(ipline[l+1:r]))

print(numlist)
