'''
123-123-123-123-123-123-123-123-1
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
'''
import operator
ops = { "+": operator.add, "-": operator.sub }
def arithmetic_arranger(x, y):
    for calc in x:
        calc = calc.split(' ')
        space = 4 - len(calc[0])
        print(" "*space + calc[0] + ' '*4, end=" ")
    print(' ')
    
    for calc in x:
        calc = calc.split(' ')
        spaceTwo = 4 - len(calc[2]) - 2
        print(" "*spaceTwo + calc[1] + " " + calc[2] + ' '*4, end=" ")
        
    print('')
    for calc in x:
        calc = calc.split(' ')
        dash = len(calc[2]) + 1
        print("-"*dash, end=" ")
    print('')
    
    for calc in x:
        calc = calc.split(' ')
        print(" "*(4 - len(str(ops[calc[1]](int(calc[0]), int(calc[2]))))) + str(ops[calc[1]](int(calc[0]), int(calc[2]))), "  ",  end=" ")
        
        
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

