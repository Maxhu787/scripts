usrinput = input().split(" ")
l = int(usrinput[0])
h = int(usrinput[1]) + 1

answers = []
for i in range(l, h):
    num = 0
    for j in str(i):
        num += (int(j) ** int(len(str(i))))
    if(num == i):
        answers.append(str(num))        
    
for i in answers:
    print(i, end=' ')
if not answers:
    print('none')
