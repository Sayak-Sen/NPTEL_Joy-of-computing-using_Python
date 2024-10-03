'''
Create a Python program to compute the sum of the first N natural
numbers {1,2,3...N}. The program should prompt the user to input the
value of N, then compute and print the sum of the first N natural
numbers.
'''

n=int(input())
temp=0
for i in range(1,n+1):
    temp=temp+i
print(temp)    
    
