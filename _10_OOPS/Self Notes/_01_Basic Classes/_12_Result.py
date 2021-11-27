class result:
    # STATE
    def __init__(self, sname, sid, marks1, marks2, marks3):
        self.sname = sname
        self.sid = sid
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    # BEHAVIOUR
    def get_stu_info(self):
        print("The Mark Details are:")
        print("Student:", self.sname,  "Student id:", self.sid,  "Marks in Science:", self.marks1, "Marks in English:", self.marks2,
              "Marks in Maths:", self.marks3)


marks = result("Karthick", 234590, 89, 95, 76)
marks.get_stu_info()