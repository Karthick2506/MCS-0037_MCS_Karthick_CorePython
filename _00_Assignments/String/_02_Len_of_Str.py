# P01. REQ : Find length of the given string

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  Retrieval
2. STATE      -->  string 
3. BEHAVIOR   -->  int  |  =   +=    |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. assign or take a sentence
3. Start reading it. 
4. While reading each char, increase the count
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")

message = 'Welcome to Python'  # static way

print("The Length of given string : ", len(message))

str_len = str(input("Enter a String"))  # Dynamic way

print("The Length of the given string is:", len(str_len))

# 2. Algorithm

print("--------2. Algorithm----------")

message = 'Welcome to python'
leng = 0
for char in message:
    leng += 1
print("The Length of given string : ", leng)

# 3 Using Functions
print("--------3 Using Functions----------")


# without parameter
def leng():
    str1 = "Welcome to Python"
    print("The Length of Given String is:", len(str1))


leng()


# With Parameter
def leng1(a):
    print("The Length of Given String is:", len(a))


leng1("Welcome to Python")

# 4 OOPS
print("--------4 Object Oriented----------")

# 5 Exception handling
print("--------5 Exception handling----------")

# 6 File Handling
print("--------6 File Handling----------")

# 7 Database interaction MVC
print("--------7 Database interaction----------")

# 8 UI Interaction
print("--------8 UI Interaction----------")
