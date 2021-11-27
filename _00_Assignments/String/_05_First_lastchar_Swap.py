# P01. REQ : First and Last Character swapping

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  Update
2. STATE      -->  string 
3. BEHAVIOR   -->  swapping  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. assign or take a string
3. Interchange the first and last character of the string. 
4. write down the interchaged string and we get the answer
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")

message = "Python"
output= message[-1] + message[1:-1] + message[0]
print("After Swapping First and Last Character:", output)





# 2. Algorithm

print("--------2. Algorithm----------")

message = "Python"
output= message[-1] + message[1:-1] + message[0]
print("After Swapping First and Last Character:", output)




# 3 Using Functions
print("--------3 Using Functions----------")
def swap():
    message = "Python"
    output = message[-1] + message[1:-1] + message[0]
    print("After Swapping First and Last Character:", output)
swap()



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