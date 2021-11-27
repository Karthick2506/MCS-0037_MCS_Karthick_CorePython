'''
Python if statement:
-------------------
If statement is the most simple form of decision-making statement.
It takes an expression and checks if the expression evaluates to True then the block of code in if statement
will be executed.
If the expression evaluates to False, then the block of code is skipped.

Syntax:
-------
if ( expression ):
  Statement 1
  Statement 2
  .
  Statement n
'''

a = 10
b = 10
if a == b:
    print("Both the values are equal")
else:
    print("Both the values are not equal")

'''Here the first block will be executed because the first condition itself is true
so here we will get a output as "Both values are equal"'''

a = 5
if a >= 10:
    print("Value a is greater than 10")
else:
    print("Value of a is lesser than 10")

'''Here the second block will be executed because the second condition is true
so here we will get a output as "Value of a is lesser than 10"'''