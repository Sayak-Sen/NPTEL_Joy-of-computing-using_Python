'''
Accept two integers m and n as input ,there are two cases consider
1. if M<N prints M
2. if M >= N subtract N from M
call the difference diff
if diff>=N then subtract N from M uodate value of diff with result of subtraction

keep doing these operation untill diff<N , print value of diff as output

'''

m=int(input("Enter value of M : "))
n=int(input("Enter value of N : "))
if m<n:
    print(m)
else:
    diff=m-n
    if diff<n:
        print(diff)
    else:
        while diff>=n:
            diff-=n
        print(diff)    
    
    