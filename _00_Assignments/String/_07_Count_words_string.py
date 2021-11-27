# P01. REQ : Count number of words in a string

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  Retrieval
2. STATE      -->  string 
3. BEHAVIOR   -->  counting  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. assign or take a string
3. Count the number of words in the string. 
4. write down the value
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")
txt = "Good morning all everybody"
output = len(txt.split())
print("The Number of Words present in the string:", output)

# 2. Algorithm

print("--------2. Algorithm----------")
txt = "Good morning all everybody welcoming you all to this program"
word_cnt = 1
for i in txt:
    if i == " ":
        word_cnt += 1
print("The Number of Words present in the string:", word_cnt)

# 3 Using Functions
print("--------3 Using Functions----------")
def word_count():
    txt = "Good morning all everybody welcoming you all to this program have a great day"
    word_cnt = 1
    for i in txt:
        if i == " ":
            word_cnt += 1
    print("The Number of Words present in the string:", word_cnt)
word_count()









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