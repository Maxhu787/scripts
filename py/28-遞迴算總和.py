# 遞迴算總和

n=10

def sum(n):
    if (n<1 ) : 
      return 0   
    return sum(n-1)+n

print(sum(n))

