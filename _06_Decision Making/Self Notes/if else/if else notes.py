'''
Python if-else statement:
-------------------------
From the name itself, we get the clue that the if-else statement checks the expression and executes the if block
when the expression is True otherwise it will execute the else block of code.
The else block should be right after if block and it is executed when the expression is False.

Syntax:
-------
if( expression ):
  Statement
else:
  Statement
'''

a=100
b=200
if(a<b):
    print("A is greater than B")
else:
    print("A is lesser than B")



num = 3
if num > 0:
    print(num, "is a positive number.")


num = -1
if num > 0:
    print(num, "is a positive number.")


var1 = 100
if var1:
   print("1 - Got a true expression value")
   print(var1)
else:
   print("1 - Got a false expression value")
   print(var1)


var2 = 0
if var2:
   print("2 - Got a true expression value")
   print(var2)
else:
   print("2 - Got a false expression value")
   print(var2)

