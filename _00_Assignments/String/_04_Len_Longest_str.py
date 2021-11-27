# P01. REQ : Length of longest string in python

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
2. assign or take a sequence of strings
3. count the number of characters of each string seperately. 
4. write down the string having the maximum length
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")

message = ['Welcome', 'to', 'Python', 'Everyone']  # static way
msg1 = max(message, key = len)
print("Longest string in the list is:", msg1)

# 2. Algorithm

print("--------2. Algorithm----------")

message = ['Welcome', 'to', 'Python', 'Everyone']
max_len = -1
for char in message:
    if message.count(char) > max_len:    # Condition
        max_len = len(message)

print("Longest string in the List:", char)



# 3 Using Functions
print("--------3 Using Functions----------")
message = ['Welcome', 'to', 'Python', 'Everyone']
# Function Structure
def sample():
    output = max(message, key = len)
    print(output)

print("The Longest String in the List is:")
sample()


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