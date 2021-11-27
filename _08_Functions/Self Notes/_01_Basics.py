'''
Functions:
----------
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.'''

'''
Syntax:
------
def function_name(parameters):
	"""docstring"""
	statement(s)
'''


'''Creating a Function:'''

def sample():
    print("Welcome")

'''Calling a Function:'''

def test():
    print("Good Morning")

test()


# function with parameter
def welcome(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    # Printing the message
    print("Hello, " + name + ". Good morning!")


# Calling the function and passing the arguments
welcome('Karthick')

# Function is mainly used for code reusability. once the functions is created we can call it anywhere
