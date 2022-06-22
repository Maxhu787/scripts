# (練習: 2-6)
ans = 35                        # 猜數字的解答
for guessChance in range(0,3):
    guess = int(input("Please input a number (1~100):")) 
#二行合併, 單引號改雙引號
    if ans == guess:
        print  ('答對了')
        break                   # 猜對後跳出 for 迴圈
    else:
        print('猜錯了')
print('遊戲 結束')
