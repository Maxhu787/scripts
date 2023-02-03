# 文字的排列組合 (接納法)

def force(): 
    data = "abc" 
    for i in range(len(data)): 
        for j in range(len(data)): 
            for k in range(len(data)): 
                if data[i] != data[j] and  data[j] != data[k] \
                    and data[i] != data[k]:  # 上面一行太長以" \"分割
                    print(data[i],data[j],data[k]) 
force() 
