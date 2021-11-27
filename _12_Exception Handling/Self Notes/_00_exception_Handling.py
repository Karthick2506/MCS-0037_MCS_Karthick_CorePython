'''
Exception:
--> Exception is a runtime error which programmers have to handle.

Exception Handling:
--> The Purpose of error handling is to make the program robust.The word robust
means Strong.A robust program does not terminate in the middle.Also, when there
is an error in the program,it will display appropriate message to the user and
continue the execution.

Steps to Follow While performing Exception:

Step1:
try:
    statements
step2:
except exceptionname:
    statements   # Handlers

step3:
finally:
    statements
'''
# Ex:
def division():
    try:
        a = int(input("Enter the Number"))
        b = int(input("Enter the Number"))
        c = a / b
        return c

    except ZeroDivisionError as e:
        print("Please Provide valid denominator", type(e))
    except Exception as r:
        print("Print the error", type(r))
    finally:
        print("Anyway Close the file")


div = division()
print("The addition of the Two numbers are", div)

# EX:
def postive():

    try:
        a = int(input("enter a number"))

        if a > 0:
            print(a, "is a Positive number")

        else:
            raise Exception("NegativeException")

    except Exception as e:
        print("Give the Exception Type", type(e))
    finally:
        print("Anyways close the file")


num = postive()

'''
def demo_no_catch():
    try:
        raise Exception('general exceptions not caught by specific handling')
    except ValueError as e:
        print('we will not catch exception: Exception')


demo_no_catch()'''

'''
eval():
--> The eval() function accepts the input in the form of list, tuple,
 dictionary.
'''
# example of syntax error:
try:
    date = eval(input("Enter a Date"))
except SyntaxError:
    print("Invalid Date Format")
else:
    print("You have entered the Correct Format")

# example for IOE
try:
    name = input("Enter a file name")
    f = open(name , 'r')
except IOError:
    print("file not found:", name)
else:
    n = len(f.readlines())
    print(name, 'has', n , 'lines')
    f.close()



