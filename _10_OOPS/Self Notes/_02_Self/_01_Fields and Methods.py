'''
Instance variables
Instance methods
'''

def func1():
    print("Function1 body")

func1()




class Employee:
    # local variables   - eid, name, sal
    # instance variables - self.eid self.name self.sal - instance variables

    def __init__(self, eid, name, sal):
        print("Self address : ", self)
        self.eid = eid
        self.name = name
        self.sal = sal

    # instance methods
    def get_edata(self):
        print("Employee information : ", self.eid, self.name, self.sal)


madhu = Employee(100, 'Karthick', 15000)
madhu.get_edata()  # Employee.get_edata(Karthick)




li1 = [1, 2, 3]  # list1 is of type class list
li1.append(100)  # list.append(li1,100)
li1.pop()        # list.pop(li1)


li1 = []
for i in range(0, 10):
    li1.append([])
print(li1)

class People:
    name = "Karthick"
    age = 26

    def detail(self):
        print(self.name)
        print(self.age)
aa = People()
aa.detail()




