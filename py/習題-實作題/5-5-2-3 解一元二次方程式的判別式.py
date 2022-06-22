# 5-5-2-3 解一元二次方程式的判別式
'''
輸入三個數字(a,b,c,代表一元二次方程式 ax**2+bx+c=0的三個係數)

請撰寫一程式，將使用者輸入的三個整數（代表一元二次方程式 ax**2+bx+c=0   的三個係數a、b、c）
然後判斷 delta= b**2-4ac 是否有解        

1. 如果 delta < 0 無解 
   傳回" Your equation has no root "        

2. 如果 delta == 0 只有一組解
   傳回 output=-b/2*a 

3. 如果 delta > 0  有兩組解
   q1=(-b+d**0.5)/(2*a)
   q2=(-b-d**0.5)/(2*a) 
   傳回組合結果output=q1+", "+q2
   最後顯示 結果1+", "+結果2


練習解:
x**2-3x+5=0
13x**2+7x+1=0 
-6x**2+4x-3=0
   
'''
a=eval(input()) # eval 函數輸入可以是運算式 如: 13  可以寫成 5+8
b=eval(input())
c=eval(input())

delta=b**2-4*a*c  # 判別式是b^2-4ac，用“Δ”表示(讀做“delta”)。定義 判別式
if delta<0:
    output="Your equation has no root."
elif delta==0:
    output=-b/2*a
    output= "Two equal root= "+str(output)
else:
    q1=(-b+delta**0.5)/(2*a)
    q2=(-b-delta**0.5)/(2*a)
    output='Two differnct rrot: {}, {}'.format(q1, q2)

print(output)







