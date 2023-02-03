# 文字的排列組合 ( 排斥法)
def force(): 
    data = "123" 
    for i in range(len(data)): 
        for j in range(len(data)):
            if (data[i] == data[j] ) :
                continue
            for k in range(len(data)):
                if data[i] == data[k] or data[j] == data[k] :
                    continue
                print(data[i],data[j],data[k]) 

force() 

