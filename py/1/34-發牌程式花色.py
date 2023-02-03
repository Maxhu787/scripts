flower='♥♠♦♣' # 花色

lenstr=len(flower)
print(lenstr)
for i in range(4):
    print(ord(flower[i:i+1]))

print(chr(9829),chr(9824),chr(9830),chr(9827))

flow=['♥','♠','♦','♣']
for i in range(4):
    print(flow[i],end=' ')

print()
# ------------------------------------------------
num='A23456789TJQK'  # 大小數字
for i in range(13):
    print(num[i:i+1], end=' ')

print()
print(list(num))

pokernumlist=list(num)
print()
for i in pokernumlist:
    print(i,end=' ')
# -------------------------------------------------
    





    
