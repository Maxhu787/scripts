# 6-7-2-2 計算應繳之稅款
'''
所得 30 萬以內課 6%
所得 30 ～ 80 萬課 13%
所得 80 ～ 150 萬課 21%
所得 150 ～300 萬課 30%
所得 300 萬以上課 40%

'''
income = int(input("所得輸入整數 (萬元)= "))
if income > 300:
    tax=income*40/100
    
elif income >= 150:
    tax=income*30/100
elif income >= 80:
    tax=income*21/100
elif income >= 30:
    tax=income*13/100
else:
    ptax=income*6/100

print("應繳之稅款=",tax,"萬元")
