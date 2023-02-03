import random

count=0 ; guess=0 ; play='y'
n=random.randint(1,100)
while (guess != n) and ((play != 'y') or (play != 'Y')):
    try:
        guess=int(input('Enter (1~100)?'))
        count = count + 1
        if (guess > n):
            print('too big')
        elif(guess<n):
            print('too small')
        else:
            play=input('Correct, continue playing(Y/N)?')
            if (play == 'n') or (play == 'N'):
                break
            n=random.randint(1,100)
            count=0
        print( 'Guess:',count,'time(s)')
    except:
        print('Please enter a number')
print(' Answer = ',n)
