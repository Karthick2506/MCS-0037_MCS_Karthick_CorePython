# REQ : Find sum of 2 given numbers

# 1. STATE
'''
num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
'''
num1 = 10
num2 = 20


# 2. BEHAVIOR
def sum(n1, n2):
    result = n1 + n2
    print("Addition : ", result)


sum(10, 20)
sum(num1, num2)
sum(5 + 5, 10 + 10)

'''
9,10 : num1,num2  ==> Variables     : 10,20      ==> values
13   : n1,n2      ==> Parameters
17,18,19 :        ==> arguments     

'''
print(100)
print(40+60)

'''
Python Default Arguments:
-------------------------
Function arguments can have default values in Python.

'''
# Passing Arguments
'''
1. Positional arguments (Required arguments)
2. Default arguments
3. Keyword arguments (Named arguments)'''

print("1. Positional arguments")
def sample(a, b, c):
    z = a + b + c
    print(z)
'''Here the value 10 will assign to a, 20 assign to b, 30 assign to c. It works base on the position'''
sample(10, 20, 30)

def great(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        print("Num1 is greater")
    elif (num2 >= num1) and (num2 >= num3):
        print("Num2 is greater")
    else:
        print("Num3 is greater")
great(8, 10, 5)  # 8 -->num1, 10 -->Num2, 5 -->Num3


print("3. positional Arguments")
def total(n1, n2):
    sum = n1 + n2
    print(sum)
total(2, 4)

'''import math
a = int(input("Enter the number"))
print(math.factorial(a))'''


def test1(mark1, mark2, mark3):
    print("The marks are", mark1, mark2, mark3)
test1(90, 76, 98) # This will take the marks and display it in a sequential order


def test2(m1, m2, m3):
    print("The marks are")
    print("The marks in english is:", m1)
    print("The marks in maths is:", m2)
    print("The marks in science is:", m3)
test2(m3 = 90, m1 = 95, m2 = 78)

'''Default Arguments'''

def defaultArg(name, f = 'Come here!'):
    print(name, f)
defaultArg('Karthick') # output here is Karthick Come here

# Second way of declaring

defaultArg('karthick', 'Good Morning') # here good morning gets overwrites.





















