'''
Python if-elif:
--------------
You might have heard of the else-if statements in other languages like C/C++ or Java.
In Python, we have an elif keyword to chain multiple conditions one after another.
With elif ladder, we can make complex decision-making statements.
The elif statement helps you to check multiple expressions and it executes the code as soon as
one of the conditions evaluates to True.

Syntax:
-------

if( expression1 ):
  statement
elif (expression2 ) :
  statement
elif(expression3 ):
  statement
.
.
else:
  statement
'''

print("***Select Your Ride***")
a = int(input("Enter Your Choice"))
if a == 1:
    print("You have Selected Bike")
elif a == 2:
    print("You have Selected Car")
elif a== 3:
    print("You have Selected Train")
else:
    print("Wrong Choice")

a = int(input("Enter your marks"))
if a >= 80:
    print("First Class")
elif a >= 70:
    print("Second Class")
elif a >= 60:
    print("Third Class")
else:
    print("Fail")
'''

Odd or Even Number Pgm:
-----------------------
'''
a = int(input("Enter your Number"))
if a%2 == 0:
    print("The Given number is an even number")
else:
    print("The Given number is odd number")

'''
Grade of a student:
-------------------
'''
m = int(input("Enter your marks"))
if m >= 80:
    print("Your Grade is A+")
elif m >= 60:
    print("Your Grade is A")
elif m >= 50:
    print("Your Grade is B")
elif m >= 35:
    print("Your Grade is C")
else:
    print("Fail")

'''
Maximum Number:
---------------
'''
a = 10
b = 30
c = 20
if (a>b and a>c):
    print("A Greater")
elif(b>c):
    print("B is Greater")
else:
    print("C is Greater")
'''
Leap Year:
---------
'''
'''year=int(input("Enter the Year:"))
if(year%4==0 and year%100!=0) or (year%400==0):
    print("The given Year is Leap Year")
else:
    print("The Given year is not a Leap Year")'''












