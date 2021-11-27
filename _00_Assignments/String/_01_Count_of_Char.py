# P01. REQ : Count Characters in string

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
3. Start Counting it. 
4. Increase the count one by one
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")

message = 'Welcome to Python'  # static way

print("The Count of E in the string is:", message.count("e"))

print("The Count of W in the string is:", message.count("w"))

print("The Count of L in the string is:", message.count("l"))

print("The Count of P in the string is:", message.count("p"))

print("The Count of O in the string is:", message.count("o"))

print("The Count of N in the string is:", message.count("n"))

print("The Count of Y in the string is:", message.count("y"))

print("The Count of T in the string is:", message.count("t"))

print("The Count of C in the string is:", message.count("c"))

# 2. Algorithm

print("--------2. Algorithm----------")

str1 = "karnataka"
dummy = []
for char in str1:
    if str1.count(char) > 1:
        if char not in dummy:
            dummy.append(char)
print("The Repeated Characters in the String are:", dummy)
print("K Occured:", str1.count("k"), "times")
print("A Occured:", str1.count("a"), "times")


# 3 Using Functions
print("--------3 Using Functions----------")
def count1():
    str2 = "Welcome to Python"
    print("The Count of E in the string is:", str2.count("e"))

    print("The Count of W in the string is:", str2.count("w"))

    print("The Count of L in the string is:", str2.count("l"))

    print("The Count of P in the string is:", str2.count("p"))

    print("The Count of O in the string is:", str2.count("o"))

    print("The Count of N in the string is:", str2.count("n"))

    print("The Count of Y in the string is:", str2.count("y"))

    print("The Count of T in the string is:", str2.count("t"))

    print("The Count of C in the string is:", str2.count("c"))

count1()

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