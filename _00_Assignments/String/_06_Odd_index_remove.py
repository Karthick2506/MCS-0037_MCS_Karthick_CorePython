# P01. REQ : Remove odd index values

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  Retrieval
2. STATE      -->  string 
3. BEHAVIOR   -->  removing  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. assign or take a string
3. Count the index value. 
4. write down the even value index
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")



# 2. Algorithm

print("--------2. Algorithm----------")
str = "programming"
output = ""
for i in range (len(str)):
    if i % 2 ==0:
        output = output + str[i]
print("After Removing index Value:", output)


# 3 Using Functions
print("--------3 Using Functions----------")
def odd_ind(str):
    res = ""
    for i in range (len(str)):
        if i % 2 == 0:
            res = res + str[i]
    print("After Removing index Value:")
    return res
print(odd_ind("programming"))







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