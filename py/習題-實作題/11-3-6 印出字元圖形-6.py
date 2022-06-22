# 11-3-6 印出字元圖形-6
'''

    *
   * *
  * * *
   * *
    *
'''

for i in range(-2,3):
    print(' '*abs(i),end='')
    for j in range(3-abs(i)):
        print(" *",end='')
    print()
