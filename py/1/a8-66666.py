from functools import reduce

def Rotate(list):                                              # 數字旋轉
    def rot(i):
        return [list[i]] + list[0:i] + list[i + 1:]
    return [rot(i) for i in range(len(list))]
   
def perm(list):                                                # 這是排列 副程式
    if list == []:
        return [[]]
    else:
        lts = Rotate(list)
        return reduce(lambda a, b: a + b, 
            [[[lt[0]] + pl for pl in perm(lt[1:])] for lt in lts])
   
for list in perm([1, 2, 3, 4,5,6,7,8,9]):
    if (list[0]==6 or list[0]==7) :                            # 減數的第一位；6 就是 7
        if ((list[4] - list[8] ==6) or (list[8]-list[4]==4)):  #  == 6 減去後最後一位是6
                                                               #  == 4 是借位，如 13-7 ; 
            n1=list[0]*10000+ list[1]*1000+ list[2]*100+ list[3]*10+ list[4]
            n2=list[5]*1000+ list[6]*100+ list[7]*10+ list[8]
            if (n1-n2) == 66666 :
                print(n1 ,"-" ,n2,"=66666")

