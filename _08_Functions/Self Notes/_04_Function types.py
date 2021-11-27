# Categories:

'''1. Function with parameters, with return type
2. Function with parameters, without return type
3. Function without parameters, with return type
4. Function without parameters, without return type'''

print("3. Function without parameters, with return type")
li = []
def even():
    for i in range (0, 20):
        a = i
        if a%2==0:
            li.append(a)
    return li
print("The List of Even numbers are:", even())

print("2. Function with parameters, without return type")

def num(a, b):
    if a > b:
        print("a is greater")

    else:
        print("b is greater")
output = num(12, 75)

print("4. Function without parameters, without return type")

def addition():
    print("The sum of all the numbers in the list is:", sum)
addition()

lis1 = [1, 2, 3, 4]
sum = 0
for i in lis1:
    sum = sum + i

def test3():
    a = 20
    b = 20
    c = a + b
    print("The addition Value is:", c)
test3()


print("1. Function with parameters, with return type")

def val(a, b):
    if a > b:
        return a
    else:
        return b
output= val (10, 8)
print("The Highest Number is:", output)

a = "Welcome to Python"
count = 0
for i in a:
    count += 1
print("The Length of the string is:", count)


'''Recursive function

# Function which calls itself is a recursive function'''

# Factorial Program

def factorial(x):
    fact = 1
    for i in range (1, x+1):
        fact = fact * i
    return fact
output = factorial(5)
print(output)