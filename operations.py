import math
def addition(a,b):
    print ('sum is:', a+b)

def subtraction(a , b):
    print ('subtractio is:', a-b)


def multiplication (a,b):
    print ('multiplication is: ', a*b)


def division (a,b):
    print ('division is:', int(a/b))


def reminder(a,b):
    print('reminder :', a % b) 

print('Welcome to Calulator : ')

print('Enter first number:')
n1 = int(input())

print('Enter second number:')
n2 = int(input())

addition(n1, n2)
subtraction(n1,n2)
multiplication(n1,n2)
division(n1,n2)
reminder(n1,n2)
math.sqrt(n1)