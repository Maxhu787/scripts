# smallest num of list
list1=[11,12,13,14,15,3]
list2=[11,12,13,14,25,20]
list3=[23,15,18,20,11,12]
list4=[18,17,19,24,15,16]

# 本題用迴圈分四次輸入:
'''
list1=[]
for i in range(4):
    ip=int(input('input='))
    list1.append(ip)
'''

small=(min(list2))
print(small)
if small == list2[5]:
    print('TRUE')
else:
    print('FALSE')

          

    
