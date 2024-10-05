'''
Write a python program that takes two variables as input from the user, say, x and y. Display the values on screen.

Then, swap the variables values with each other. The initial value of x must be stored in y and vice versa. Display these values on screen next.

'''
x=input('first value  ')
y=input('second value ')
print('first value is ',x)
print('second value is ',y)
z=x
x=y
y=z
print('after swapping')
print('first value will be ',x)
print('second value will be ',y)