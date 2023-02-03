# 猜數字遊戲
import random
c=0 ; guess=0 ; play='y'
n=random.randint(1,100)
while (guess != n) and ((play != 'y') or (play != 'Y')):
    guess=int(input('請輸入 (1~100)？'))
    c=c+1
    if (guess > n):
        print('too big')
    elif(guess<n):
        print('too small')        
    else: 
        play=input('你對猜了，要不要繼續猜(Y/N)？')
        n=random.randint(1,100)
        c=0
        if  (play == 'n') or (play == 'N'):
            break        
    print( '你已經猜了:',c,'次')    
print(' 答案是:',n)
