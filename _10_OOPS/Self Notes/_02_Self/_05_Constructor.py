'''Constructor is used for initializing the instance members when we create the object of a class.'''

"""For example:
Here we have a instance variable num which we are initializing in the constructor.
The constructor is being invoked when we create the object of the class (obj)."""

class DemoClass:
    # constructor
    def __init__(self):
        # initializing instance variable
        self.num=100

    # method
    def read_number(self):
        print(self.num)

# creating object of the class. This invokes constructor
obj = DemoClass()

# calling the instance method using the object obj
obj.read_number()   # Here the Output is 100

"""Types of Constructors in Python
* Default Constructor
* Parameterized Constructor
"""

# Default Constructor:

class DemoClass:
    num = 55
    # method
    def read_number(self):
        print(self.num)

# creating object of the class. This invokes constructor
obj = DemoClass()

# calling the instance method using the object obj
obj.read_number()


# Parameterized Constructor

class DemoClass:
    num = 101

    # parameterized constructor
    def __init__(self, data):
        self.num = data

    #  method
    def read_number(self):
        print(self.num)


# creating object of the class
# this will invoke parameterized constructor
obj = DemoClass(55)

# calling the instance method using the object obj
obj.read_number()

# creating another object of the class
obj2 = DemoClass(66)

# calling the instance method using the object obj
obj2.read_number()


"""Features of Python Constructors: 

In Python, a Constructor begins with double underscore () and is always named as __init_().
In python Constructors, arguments can also be passed.
In Python, every class must necessarily have a Constructor.
If there is a Python class without a Constructor, a default Constructor is automatically created without any arguments and parameters."""
"""
Counting the number of objects of a class
The constructor is called automatically when we create the object of the class. Consider the following example."""
"""
class Student:    
    count = 0    
    def _init_(self):    
        Student.count = Student.count + 1    
s1=Student()    
s2=Student()    
s3=Student()    
print("The number of students:",Student.count)    
"""


class Employees():

    def _init_(self, Name, Salary):
        self.Name = Name
        self.Salary = Salary

    def details(self):
        print("Employee Name : ", self.Name)
        print("Employee Salary: ", self.Salary)
        print("\n")


first = Employees("Khush", 10000)
second = Employees("Raam", 20000)
third = Employees("Lav", 10000)
fourth = Employees("Sita", 30000)
fifth = Employees("Lucky", 50000)

first.details()
second.details()
third.details()
fourth.details()
fifth.details()



class Employee:
    def _init_(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))


emp1 = Employee("John", 101)
emp2 = Employee("David", 102)

# accessing display() method to print employee 1 information

emp1.display()

# accessing display() method to print employee 2 information
emp2.display()

# Default constructor
class Employee:

    def _init_(self):  # Default constructor
        pass  # to perform any generic action

    def getedata(self, eid, sal):
        print("Employee Data", eid, sal)


karthick = Employee()
karthick.getedata(101, 10000)  # Employee.getedata(madhu,101,10000)

# while defining class, default constructor is not mandatory. Python give automatically


# Employee CRUD Operations

'''
REQUIREMENT :
1. Create an employee with eid,name,sal  #
2. Retrieve emp details 
3. Give hike for employee based on experience
    Acceptance Criteria : 0 to 2 exp  => 5% hike
                          2 to 3 exp  => 10% hike
                          3 to 5 exp  => 20% hike
                          5+          => 30% hike

4. Delete emp once he exits from company

GUI  -->  Backend             ---> Database

UI  --->  Python/Java/.Net    --->  Oracle/Postgresql/Mysql/Mongodb
'''

print("-----------Employee hike---------------")


class Employee:
    # create employee
    def _init_(self, eid, name, sal):  # emailid,mobiileno,perm_address,pre_add,joining_date,bloodgr,gendder
        self.eid = eid
        self.name = name
        self.sal = sal

    # 2. Retrieve emp details
    def get_emp_info(self):
        print("Employee details : ", self.eid, self.name, self.sal)

    # 3. Update emp sal based on exp
    '''
        3. Give hike for employee based on experience
        Acceptance Criteria : 0 to 2 exp  => 5% hike
                              2 to 3 exp  => 10% hike
                              3 to 5 exp  => 20% hike
                              5+          => 30% hike
    '''

    def update_emp_sal(self, exp):
        # Server validations
        if exp < 0:
            print("Please enter valid experience.")
            return None
        if exp >= 0 and exp < 2:
            hike = (self.sal * 5) // 100
            self.sal = self.sal + hike
        elif exp >= 2 and exp < 3:
            hike = (self.sal * 10) // 100
            self.sal = self.sal + hike
        elif exp >= 3 and exp < 5:
            hike = (self.sal * 20) // 100
            self.sal = self.sal + hike
        elif exp >= 5:
            hike = (self.sal * 30) // 100
            self.sal = self.sal + hike
        print("Employee  after hike : ", self.eid, self.name, self.sal)

    def delete_emp(self):
        pass


# Data hard coding
satish = Employee(100, 'satish', 1500000)
satish.get_emp_info()
satish.update_emp_sal(4)

'''
UI PAGE:
---------
EmmpID: 101
name  : satish
exp   : -10 
Mobileno : 34232443243

# client validations 
# server validations
'''
"""class Student: 

    # Constructor - parameterized  
    def _init_(self, name):  
        print("This is parametrized constructor")  
        self.name = name  
    def show(self):  
        print("Hello",self.name)  
student = Student("John")  
student.show()
 """
# Positional arguments

"""
class Employee:
    # Parameterized Constructor
    def _init_(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def getedata(self):
        pass

satish = Employee(200, 'satish', 10000)
"""

'''
# Defining Constructor
    - Default constructor
    - Parameterized constructor
            - Positional arguments
            - Default arguments
            - keyword arguments

'''
# Default arguments example
"""
class Employee:
    # parameterized constructors
    def _init_(self, eid=None, name=None, sal=None):  # Constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal

    def getedata(self):
        print("Employee info : ", self.eid, self.name, self.sal)


satish = Employee()
satish.getedata()

sam = Employee(201)
sam.getedata()

venkat = Employee(201, 'Chandra Sekhar')
venkat.getedata()

ravi = Employee(200, 'MadhuN', 10000)
ravi.getedata()

raju= Employee(name='Farooq', sal=20000)
raju.getedata()


class Student:
    def _init_(self):
        print("The First Constructor")

    def _init_(self):
        print("The second contructor")


st = Student()  
"""
"""
lass Student:  
    def _init_(self, name, id, age):  
        self.name = name  
        self.id = id  
        self.age = age  

    # creates the object of the class Student  
s = Student("John", 101, 22)  

# prints the attribute name of the object s  
print(getattr(s, 'name'))  

# reset the value of attribute age to 23  
setattr(s, "age", 23)  

# prints the modified value of age  
print(getattr(s, 'age'))  

# prints true if the student contains the attribute with name id  

print(hasattr(s, 'id'))  
# deletes the attribute age  
delattr(s, 'age')  

# this will give an error since the attribute age has been deleted  
print(s.age)  
"""


"""class Student:

    def _init_(self,name,id,age):
        self.name = name;
        self.id = id;
        self.age = age

    def display_details(self):
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))

s = Student("John",101,22)
print(s._doc_)
print(s._dict_)
print(s._module_)"""




