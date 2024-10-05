'''
Accept three positive integers as inputs and check if they form the sides of a right angle

print Yes if they form print No if they do not 

'''
import math as m
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

#maximum length of a triangle
if a>b and a>c:
    a,c=c,a
elif b>a and b>c:
    b,c=c,b
    
if c==m.hypot(a,b):
    result=True
else:
    result=False

if result:
    print("Yes")
else:
    print('NO')            
    