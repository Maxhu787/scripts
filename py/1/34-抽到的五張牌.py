# 發牌
import itertools, random

# 花色

deck = list(itertools.product(range(1,14),['黑桃','紅心','方塊','梅花'])) # list 未洗牌
print(deck)
print('\n\n\n')

for i in range(52):
   print(deck[i], end='')
   if (i+1) % 4 == 0 :
      print()
print('\n\n\n')

for i in range(0,52):
    print(deck[i][0], end=' ')
print('\n\n\n')

for j in range(0,4):
    print(deck[j][1], end=' ')
print('\n\n\n')

deck0=set(itertools.product(range(1,14),['黑桃','紅心','方塊','梅花']))  # set 已經洗牌 
print(deck0)
print('\n\n\n')

# 洗牌
random.shuffle(deck)

# 抽五張牌
print("所抽到的五張牌是:")
for i in range(5):
   print(deck[i][1],":",deck[i][0])
