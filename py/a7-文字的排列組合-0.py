# 三個文字的排列

def perm(a, k=0):
   if k == len(a):
      print (k,a)
   else:
      for i in range(k, len(a)):
         a[k], a[i] = a[i] ,a[k];print(k,i,"=",a[k],a[i])
         perm(a, k+1)
         a[k], a[i] = a[i], a[k];print(k,i,"=",a[k],a[i])

perm([1,2,3])
