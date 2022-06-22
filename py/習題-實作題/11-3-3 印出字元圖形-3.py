# 11-3-3 印出字元圖形-3
'''
a
ab
abc
abcd
abcde
abcd
abc
ab
a
'''

for i in range(-4,5):
    for j in range(5-abs(i)):
        print(chr(97+j),end='')
    print()
