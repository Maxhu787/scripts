# 三個文字的排列

def perm(a, k=0):
   if k == len(a):
      print (a)
   else:
      for i in range(k, len(a)):
         a[k], a[i] = a[i] ,a[k]
         perm(a, k+1)
         a[k], a[i] = a[i], a[k]

perm([1,2])
