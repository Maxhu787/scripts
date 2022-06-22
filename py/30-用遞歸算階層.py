# 用遞歸算階層

def recu_f(n):
   if n == 1:
       return n
   else:
       return n*recu_f(n-1)

num = 6
print(num,"階層= ",recu_f(num))
