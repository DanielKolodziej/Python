from itemChecker import itemRepeaterChecker
import random

#hard code inventory items 
a=1
b=2
c=3

random.seed()
#generate random inventory item 1 
x= random.randint(1,5)
print ("Random gen #:",x)

'''
pass x value to func
get result of x back locally
'''
x = itemRepeaterChecker(x,a,b,c) 
#show non repeated inventory items
print(a,b,c,x)
#generate random inventory item 2
y= random.randint(1,10)
print (y)

'''
pass x value to func
get result of y back locally
'''
y = itemRepeaterChecker(y,a,b,c,x) 
#show non repeated inventory items
print(a,b,c,x,y)


#Further example: Verifying random generated values
print("\nVerifying random generated values")
print("*" * 32)
import random
#hard code inventory items 
a=1
b=2
c=3

#generate random inventory item 1
x= random.randint(1,5)
print ("Random gen #:", x)

'''check if x is repeating an inventory item (a b or c)'''
flg=True
while flg:
       for val in [a,b,c]:
        #regenerate x
        if x in [a,b,c]: #x == val: --not 100% accurate 
            x = random.randint(1,7)
            print("new x:",x)
        else:
            flg=False
print(a,b,c,x)

