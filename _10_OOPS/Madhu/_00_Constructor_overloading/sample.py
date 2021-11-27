

class Employee:

    def __init__(self, eid=10, name='karthick', sal=1000):  # constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal
        print(self.eid, self.name, self.sal)

# Constructor Overloading
madhu = Employee()
madhu = Employee(100)
madhu = Employee(101, 'Karthick')
kiran = Employee(102, 'Raja', 20000)