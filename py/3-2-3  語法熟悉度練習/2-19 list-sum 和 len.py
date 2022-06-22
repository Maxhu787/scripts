# (練習: 2-19)
scores =[20,40,60,80,100]
# scores =[20,40,60,80,100]
print('學科分數：', end=' ')
for grade in scores:
    print(grade,end=' ')
print(end='\n')
avg = sum(scores)/len(scores)
print('平均=：', avg)

print('新的分數:',end='')
for grade in range(0,len(scores)):
    scores[grade] = ((scores[grade]**0.5)*10) # 開平方 x 10
    print('%.2f' % scores[grade]  ,end=' ')  
print(end='\n')
n_avg = sum(scores)/len(scores)

print('新平均: %.5f' % n_avg)
