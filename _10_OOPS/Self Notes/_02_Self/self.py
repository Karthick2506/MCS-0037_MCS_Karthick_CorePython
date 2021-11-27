"""Self"""
'''
self represents the instance of the class.
By using the “self” keyword we can access the attributes and methods of the class in python.
It binds the attributes with the given arguments.
The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes.

Its simply the first parameter of any function in the class
'''

'''i is multiple of 5 and 3 print "Modern Solutions", if i is multiple by 3 not 5 print modern i is multiple of 5 not 3 print solution 
if i not multiple by 5 and 3 print the value of i'''

x = int(input("Enter a Number"))
for i in range(1, x+1):
    if i % 5 == 0 and i % 3 == 0:
        print("Modern Solutions")
    elif i % 3 == 0 and i % 5 != 0:
        print("Modern")
    elif i % 5 == 0 and i % 3 != 0:
        print("solution")
    elif i % 3 != 0 and i % 5 != 0:
        print(i)


