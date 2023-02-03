year=int(input("year="))
f=0
if year%4 ==0 :
    f=1
if year%100==0:
    f=0
if year%400==0:
    f=1

if f==1 :
    print( year,"是閏年!")
else:
    print( year,"不是閏年!")
