import random

#incl. function to check repetitive inventory items

def itemRepeaterChecker(checker,*args):
       '''check if x is repeating an inventory item (a b or c)'''
       flg=True
       while flg:
              for val in args:
                     #regenerate x
                     if checker in args:
                            checker = random.randint(1,7)
                            print("new x:",checker)
                     else:
                            flg=False
       return checker  #return x value

