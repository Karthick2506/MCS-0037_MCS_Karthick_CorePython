'''
Python Class Variables

A Python class variable is shared by all object instances of a class. Class variables are declared when a class is being constructed. They are not defined inside any methods of a class.

Because a class variable is shared by instances of a class, the Python class owns the variable. As a result, all instances of the class will be able to access that variable. Class variables are shared by all instances that access the class.

Here is an example of a class variable in Python:

'''

class Employee:
	emp = "Karthick"


"""In this example, we declare a class variable called emp. This class variable is assigned to the class Employee.

Class variables are useful because they allow you to declare a variable when a class has been built,
which can then be used later in your class
"""
"""
Accessing a Class Variable in Python

Now that we’ve declared a class variable, we can access it when we create an object of our class.
So, if we want to create a new class instance and see the value of the menu_type variable, we could use this code:"""

class Employee:
	emp = "Karthick"

emp_obj = Employee()
print(Employee.emp)

# Our code returns: Karthick.

"""
Changing a Class Variable

Class variables can also be changed, just like any other type of variable. To do so, you can use this code:"""

class Employee:
	emp = "Karthick"

emp_obj = Employee()
Employee.emp = "Raja"
print(Employee.emp)


"""Our code returns: Raja. In this example, we have declared an instance of our class called emp_obj.
Then, we assign the value of the Employee.emp class variable to be equal to Raja.
This changes the value of the variable. 

We print out the new value of the emp variable to the console using a Python print statement.

"""
