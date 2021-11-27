# P01. REQ : print the largest number in the list

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  retrieve
2. STATE      -->  List 
3. BEHAVIOR   -->  display  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. write a list 
3. pick the largest number and write down the result.
'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")
list1 = [1,2,3,4,5,6]
largest_no = (max(list1))
print("The Largest number in the list is:", largest_no)


# 2. Algorithm
print("--------2. Algorithm----------")
list1 = [1,2,3,4,5,6]
largest_no = list1[0]
for i in range (1, len(list1)):
    if list1[i] > largest_no:
        largest_no = list1[i]
print("The Largest number in the list is:", largest_no)







# 3 Using Functions
print("--------3. Functions----------")
def large():
    list1 = [1, 2, 3, 4, 5, 6]
    largest_no = list1[0]
    for i in range(1, len(list1)):
        if list1[i] > largest_no:
            largest_no = list1[i]
    print("The Largest number in the list is:", largest_no)
large()




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