#  Python Program to find the area of triangle

a = 5
b = 6
c = 7

s = (a + b + c) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

#  python program finding square root
print('enter your number')
n = int(input())
import math
print(math.sqrt(n))




#  Python program to swap two variables
x = 5
y = 10

swap = x
x = y
y = swap

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

# Program to generate a random number 
import random
print(random.randint(1,10))

# to convert kilometers to miles
1 KILOMETER = O.621371 MILES
kilometers = float(input("Enter value in kilometers: "))

conv_factor = 0.621371

miles = kilometers * conv_factor
print('{} kilometers is equal to {} miles'.format(kilometers, miles))


#  python programme to check leap years
print(' please enter year')
year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap year')      
        else:
            print(f'{year} is not a leap year')
    else:
        print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

# proramme to print table
print('Enter your number')
n= int(input())
for i in range (1, 11):
    print('{} * {} = {}'.format(n, i, n*i)) 


# find sum of natural numbers
n = int(input())
s = n*(n+1)/2
print(s)

# calculator

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
