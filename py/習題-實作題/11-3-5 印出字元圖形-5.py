# 11-3-5 印出字元圖形-5

'''
abcdefghi
 b     h
  c   g
   d f
    e
   d f
  c   g
 b     h
abcdefghi

'''

for i in range(-4,5):
    for j in range(-4,5):
        if i==-4 or i==4 :
            print(chr(101+j),end="")
        elif (abs(i) == abs(j) ):
            print(chr(101+j),end="")
        else:
            print(" ",end="")
    print()

