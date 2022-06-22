#使用函數找可被 12 整除的數字

r_List = [120,123,202,84,5,36,21 ]

r = list(filter(lambda x: (x % 12 == 0), r_List))
print("可被 12 整除的數=",r)
