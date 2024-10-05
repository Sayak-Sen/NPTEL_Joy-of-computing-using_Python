#Armstrong Number

num=input("enter a number : ")
n=len(num)
num=int(num)
tempnum=num
temp=0
if n>0:
    while num!=0:
        r=num%10
        temp=temp+r**n
        num=num//10
    if temp==tempnum:
        print(True)
    else:
        print(False)  
else:
    print('Not a armstrong number')
  