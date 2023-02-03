# (練習: 2-22)  
n=[]
for i in range(0,10):
    i = int(input('分別輸入10 個數值:'))
    n.append(i)
print(n)
print(end='\n')

'''
for i in range(0,10):          # 可以檢視內容
    print('n [',i,'] =',n[i])
'''

for questions in range(0,3):
    a = int(input('從第幾個: '))
    b = int(input('加到第幾個: '))
    print(a,'到',b, '的總和=',sum(n[a-1:b]))
    print(end='\n')
