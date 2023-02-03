#找 1 ~ 100 所有的質數
for num in range(2,16):
    # print('num=',num)
    for i in range(2, num):
        # print('i=',i)
        if num % i == 0:
            break
    else:
        print ( num, end=' ')
