#n th element of arithmatic sequence
'''
Create a Python program to determine the nth element of an arithmetic
sequence where the first term a is 7 and the common difference d is 11.
The program should prompt the user to input the value of n, then compute
and print the nth element of the sequence.

'''
a=7
d=11
term=int(input("n th element is : "))
ele=0
for i  in range(1,term+1):
    ele=a+(i-1)*d
print(ele)
