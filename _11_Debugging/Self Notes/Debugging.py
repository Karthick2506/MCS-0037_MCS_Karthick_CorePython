"""Debugging is the process of systematically removing errors, or bugs, from your code.
Python has functionalities that can assist you when debugging.
The standard debugging tool in Python is pdb (Python DeBugger) for interactive debugging"""

a = int(input("Enter a Number"))
if a % 2 == 0:
    print("The given number is an Even Number")
else:
    print("The given number is not a Even Number")

"""

to using pdb is causing the interpreter to enter the debugger when you want it to.
There are a few different ways to do that,
depending on your starting conditions and what you need to debug.


"""

import pdb
x=8
def power_of_itself(a):
      return a**a
pdb.set_trace()
seven=power_of_itself(7)
print(seven)
three=power_of_itself(3)
print(three)

# Program to print Multiplication
# table of a Number
n=5
for x in range(1,11) :
    print( n , '*' , x , '=' , n*x )


# Python Program to print Multiplication Table
# We want to debug the for loop so we use
# set_trace() call to pdb module

import pdb


# It means , the Start of Debugging Mode
pdb.set_trace()

n=5
for x in range(1,11) :
    print( n , '*' , x , '=' , n*x )

import pdb

def make_sample():
    pdb.set_trace()
    return "I don't have time"

print(make_sample())

class MyObj(object):

    def _init_(self, num_loops):
        self.count = num_loops

    def go(self):
        for i in range(self.count):
            print (i)
        return





import pdb

def f(n):
    for i in range(n):
        j = i * n
        print (i, j)
    return



import pdb

def calc(i, n):
    j = i * n
    return j

def f(n):
    for i in range(n):
        j = calc(i, n)
        print (i, j)
    return

import pdb


def addition(a, b):
	answer = a + b
	return answer


pdb.set_trace()
x = input("Enter first number : ")
y = input("Enter second number : ")
sum = addition(x, y)
print(sum)


def multiply(a, b):
	answer = a * b
	return answer


x = input("Enter first number : ")
y = input("Enter second number : ")
result = multiply(x, y)
print(result)


def addition(a, b):
	answer = a + b
	return answer


x = input("Enter first number : ")
y = input("Enter second number : ")
sum = addition(x, y)
print(sum)


# importing pdb
import pdb

# make a simple function to debugg
def fxn(n):
	for i in range(n):
		print("Hello! ", i+1)


# starting point to debugg
pdb.set_trace()
fxn(5)


# a simple function
def fxn(n):
	for i in range(n):
		print("Hello! ", i+1)


# using breakpoint
breakpoint()
fxn(5)

 # Printing Variables or expressions

# importing pdb
import pdb

# define recursive function
def rec_fxn(r):
	if r > 0:

		# set trace
		pdb.set_trace()
		rec_fxn(r//2)
	else:
		print("recursion stops")
	return

# set trace at start
pdb.set_trace()
rec_fxn(5)