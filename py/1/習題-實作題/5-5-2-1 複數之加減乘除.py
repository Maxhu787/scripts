# 5-5-2-1 複數之加、減、乘、除

'''
加法: (a + bi) + (c + di) = (a + c) + (b + d)i 
減法: (a + bi) − (c + di) = (a − c) + (b − d)i 
乘法: (a + bi) (c + di) = ac + bci + adi + bdi2 = (ac − bd) + (bc + ad)i 
除法: (a + bi)/(c + di)=((ac+bd)/(c2+d2)) + ((bc+ad)/(c2+d2))i
'''

a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=int(input('d='))

'''
a=5;b=-4;c=2;d=6
'''

print("加法: (a + bi) + (c + di) = ",a+c,"+",b+d,"i")
print("減法: (a + bi) − (c + di) =",a-c,"+",b-d,"i")
print("乘法: (a + bi) (c + di) =" , (a*c-b*d) ,"+", (b*c+a*d),"i") 
print("除法: (a + bi)/(c + di)=",((a*c+b*d)/(c*c+d*d)) ,"+",((b*c+a*d)/(c*c+d*d)),"i") 
