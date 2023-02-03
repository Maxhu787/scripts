# While 印出費氏數列(一維)
p=[]
p.append(0)
p.append(1)
n=1000
a,b=0,1
while  a+b < n:
    c=a+b
    p.append(c)
    a,b=b,c          
print(p)
