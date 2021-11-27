"""
# Encapsulation:

Encapsulation is one of the four fundamental concepts in object-oriented programming including abstraction,
encapsulation, inheritance, and polymorphism.

Encapsulation is the packing of data and functions that work on that data within a single object.
By doing so, you can hide the internal state of the object from the outside. This is known as information hiding.

A class is an example of encapsulation. A class bundles data and methods into a single unit.
And a class provides the access to its attributes via methods.

The idea of information hiding is that if you have an attribute that isn’t visible to the outside, you can control the access to its value to make sure your object is always has a valid state.
"""


class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)


person = Person('Karthick', 30)
# accessing using class method
person.display()
# accessing directly from outside
# print(person.name)
# print(person.age)

"""Methods to Control Access

There are multiple methods that are offered by Python to limit variable and method access across the program.

Using Single Underscore
-----------------------

A common Python programming convention to identify a private variable is by prefixing it with an underscore.
Now, this doesn’t really make any difference on the compiler side of things.
The variable is still accessible as usual. But being a convention that programmers have picked up on,
it tells other programmers that the variables or methods have to be used only within the scope of the class."""


class Person:
    def __init__(self, name, age=0):
        self.name = name
        self._age = age

    def display(self):
        print(self.name)
        print(self._age)
# If we use double underscore before age it will become private variable and we cannot access that from outside.


person = Person('Karthick', 30)
person = Person('Karthick')

# accessing using class method
person.display()
# accessing directly from outside
#print(person.name)
#print(person._age)

"""class Even:
    def __init__(self, a):
        self.a = a
    def check(self):

        if self.a%2 ==0:
            print("Even Number")
        else:
            print("Odd Number")
aa = Even(int(input("Enter a Number")))
aa.check()"""


class Even:
    a = int(input("Enter a Number"))

    def check(self):
        if self.a%2 == 0:
            print("Even Number")
        else:
            print("Odd Number")
aa = Even()
aa.check()



