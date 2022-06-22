list5=[1,2,3,4,5,6,7,8,9,10]
print(list5)

list6= [('Jan',1),('Feb',2),('Mar',3),('Apr',4),('May',5),('Jun',6)] 
print(list6[0][0], list6[0][1],list6[3][0],list6[3][1])

for i in range(2):
    for j in range(6):
        print(list6[j][i],end=' ')
    print()
