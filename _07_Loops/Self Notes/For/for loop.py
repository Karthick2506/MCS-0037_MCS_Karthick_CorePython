'''
For Loops:
----------
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in
other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

'''

# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

for i in numbers:
    print(i)

# print 1 to 100 using for loop
for i in range(10):
    print("sequence numbers ",i)

#direct given input
a=10
for i in range(a):
    print(i)

# user give input

a = int(input("you enter only integer numbers"))
for num in range(a):
    print(num)


# two user inputs
a=int(input("enter a number"))
b=int(input("enter b number"))
for num in range(a,b+1):
    print(num)

# string
for i in "kumar":
    print("sequnece of name",i)

print('-----------using for in list------------------')
for i in [1,2,3,4,5,6]:
    print(i)

print('--------for loop using numbers in string--------------')
for i in "12345":
    print(i)

print("---------using for loop in tuple -----------------------")

for i in (1,2,3,4,5,6):
    print(i)

print("------using for loop in set------------------------------")
for i in {10,20,30,40,50}:
    print(i)


print("---------------using for loop in dictionary------------------------------")
for i in {'name':'kumar','id':27,'company':'MCS','location':'banglure'}:
    print(i)  # only gives keys

data = {'name': 'kumar','id': 27,'company': 'MCS','location': 'banglure'}
for i in data:
    print(i)  # only gives keys
for key, value in data.items():
    print(key,value)
print(data['name'])


print('---------for loop using list----------------')
list =[1,2.0,"kumar",4,8,90.20]
print(list)
for i in list:
    print(i)


print("----------for loop using tuple-------------")
data = (1,2,3,10.08,'yuvi',20,145)
for tup in data:
    print(tup)

print("----------for loop using set--------------------")
data = {1,4,9,'kiran','sai',50.09}
for i in data:
    print(i)


print('--------print even numbers using for loop---------------')

num = int(input("enter any number:"))
for i in range(num+1):
    if i%2==0:
        print("even number is ",i)
print()



print("-------------print even numbers and store in list----------")
list = []
num = int(input("enter any number:"))
for i in range(num):
    if i%2 == 0:
        list.append(i)
print("even numbers",list)

print('----------print odd numbers and store in  list--------------')

list =[]
num = int(input("enter any number:"))
for i in range(num+1):
    if i%2==1:
        list.append(i)
print("odd numbers ",list)


print('--------print odd and even numbers and store in list---------')

even = []
odd =[]
prime = []
num = int(input("enter any number:"))
for i in range(num):
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
        if i%5!=0 and i%3!=0:
            prime.append(i)


print("even numbers",even)
print("odd numbers ",odd)
print("prime numbers",prime)


print('---------membership in list(compare two list--------------')
list = [1,2,3,4,5]
list1 =[1,2,3,4,5,6,9]
for i in list:
    for j in list1:
        if i==j:
            print("same",i)
else:
    print("not same",i)

print("--------print table----------------")

num = int(input("which table do you want:"))
num1 = int(input('enter range of a number'))
for i in range(1,num1+1):
    print(num,'x',i,'=',(num * i))

for i in [1,2,23]:
    print(i,end=' ')

print('-----------------using for loop in dictionary-------------------')
data = {'name':'yuvi','id':12,'location':'hyd'}
print(data)
for i in data:
   # print(i)    # its print only keys
   # print(data[i])  # its print only values
    print(i,':',data[i])


marks = {'telugu':80,'english':60,'maths':80}
student = ['kumar','yuvi','kiran']
for s in student:
    for key,values in marks.items():
            print(s,key,values)


print("----------nested if and for loop----------------")
name = input("enter your name:")
roll_no = int(input("enter your roll number: "))
if name == "kumar":
    if roll_no == 27:
        print("your ssc marks ")
        list = []
        marks = {'telugu': 80, 'hindi': 68, 'english': 60, 'maths': 80, 'social': 88, 'science': 95}
        for key, value in marks.items():
            print(key, value)
            list.append(value)

        print("your percentage :", sum(list)//6)

    else:
        print("your roll number is not matched")
else:
    print("please enter valid name")

list = ['kumar','hari','kiran','shiva','satti']
list1 =[1,2,3,4,5,6,'satti']
for i in list:
    for j in list1:
        if i == j:
            print(i,'matched')
        else:
            print(" not _matched ")




print("-------------print length of the list------------------")

len = 0
list = [1,2,3,4,68,90]
for i in list:
    len+=1
print(len)

list =[1,2,3,5,6]
for i in range(len(list)):
    print(i)


print('--------------------print sum of the items in  given list----------')

sum = 0
list =[1,2,3,34,2,123]
for i in list:
    sum = sum + i
print("sum of total list is",sum)


list = [1,2,'kumar','123',10.09]
for i in list:
    if i =='kumar':
        print("---found---",i)
        print('found',list.index('kumar'))
        list[2]='yuvi'
print(list)

data = ['kumar',10,98,19.89,'kiran',[1,2,4,5],(10,19,20),{1,2,3,4,5},{'name': 'kumar'}]
for i in data:
    print(i)
a=data[0]
print(a)
for i in a:
    print(i)

b=data[6]
print(b)
a=list(b)
print(a)
a.append(10)
print(a)
b=a.copy()
print(b)

print('-----------------------------break----------------------------')

# print 1 to 100
# divisible by 9 and
# first 5 numbers i want

count=0
for i in range(1,101):
    if i%9 == 0:
        print(i)
        count+=1
        if count == 5:
            break
print()
# print 1 to 100
print('-------------------print 1 to 100 --------------------')
for i in range(101):
    print(i)
    if i == 40:
        print("------matched-----")
        break
print('------end-------')
