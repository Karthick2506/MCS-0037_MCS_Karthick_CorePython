'''
Nested if statement:
--------------------
A nested if is an if statement that is the target of another if statement.
Nested if statements mean an if statement inside another if statement.
Python allows us to nest if statements within if statements.
i.e, we can place an if statement inside another if statement.
There may be a situation when you want to check for another condition after a condition resolves to true.
In such a situation, you can use the nested if construct.
In a nested if construct, you can have an if...elif...else construct inside another if...elif...else construct.

Syntax:
-------

if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   elif expression4:
      statement(s)
   else:
      statement(s)
else:
   statement(s)
'''

x = 200
if x < 300:
    print("X is Less than 300")
    if x == 100:
        print("It is 100")
    if x == 150:
        print("It is 150")
    if x == 200:
        print("x is equal to 200")
else:
    print("could not find the number")


a=int(input("Enter the Marks"))
if a == 1:
    print("You have passed the examination")
    print("1.Continue  2.Discontinue")
    choice = int(input("Enter your Choice"))
    if choice == 1:
        print("you have choose to continue")
        print("1. higher secondary  2.Diploma")
        a = int(input("Enter your Choice"))
        if a == 1:
            print("Please select the Group")
            b = int(input("Enter your choice to select the group"))
            if b == 1:
                print("You choose MPC")
            else:
                print("You choose BiPC")
        else:
            print("Please Select the Diploma Course")
            c = int(input("Enter your choice to select the Diploma Course"))
            if c == 1:
                print("You choose CS Department")
            else:
                print("You choose ECE Department")
    else:
        print("You have choose to discontinue")
else:
    print("You have failed the examination")
    print("1.Retry  2.Discontinue")
    f = int(input("Enter your choice"))
    if f == 1:
        print("Please fill the reappearing form")
    elif f == 2:
        print("you have choose to discontinue")











