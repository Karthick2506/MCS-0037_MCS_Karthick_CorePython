class Base:
    def fun1(self):
        print("base class")
class div1(Base):
    def fun2(self):
        print("Derived class 1")
class div2(Base):
    def fun3(self):
        print("Derived class 2")
class div3(div1,div2):
    def fun4(self):
        print("Derived class 3")



d3=div3()
d3.fun1()
d3.fun2()
d3.fun3()
d3.fun4()


class karthi:
    def __init__(self,name1,name2):
        self.a=name1
        self.b=name2
    def c(self):
        print(self.a,self.b)
x=karthi("John","Raja")
x.c()
x=karthi('HI','WELCOME')
x.c()

class Karthick:
    def first(self):
        p = 3.14
        r = float(input("Enter the radius of circle"))
        b = p * r * r
        print("Area of circle is:")
        print(b)

class Raja(Karthick):
    def second(self):
        s = int(input("Enter the side values of square"))
        t = s * s
        print("The area of square is")
        print(t)

a = 0
d = Raja()
while a <= 3:
    print("1. Circle")
    print("2. Square")
    print("3. Exit")
    a = int(input("Enter your choice"))
    if a == 1:
        print("Circle")
        d.first()
    if a == 2:
        print("Square")
        d.second()
    if a == 3:
        print("Exit")