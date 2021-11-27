"""Python Instance Variables

Python instance variables are owned by an instance of a class.
The value of an instance variable can be different depending on the instance with which the variable is associated.

This means that the value of each instance variable can be.
This is unlike a class variable where the variable can only have one value that you assign.
Instance variables are declared inside a class method.

Here is an example of two instance variables in Python:"""

class CoffeeOrder:
	def __init__(self, coffee_name, price):
		self.coffee_name = coffee_name
		self.price = price

"""
Assinging Values to an Instance Variable in Python

We can assign values to an instance variable when we declare a class. We do this by specifying the values we want to assign as arguments when we declare the class. Suppose we want to create an instance of our class with the following values: 
•coffee_name = “Espresso”
•price = 2.10

We could create this instance using the following code:"""

class CoffeeOrder:
	def __init__(self, coffee_name, price):
		self.coffee_name = coffee_name
		self.price = price

customer_order = CoffeeOrder("Espresso", 2.10)
print(customer_order.coffee_name)
print(customer_order.price)
