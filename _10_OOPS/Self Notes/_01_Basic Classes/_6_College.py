class college:
    # STATE
    def __init__(self, sname, sid, department):
        self.sname = sname
        self.sid = sid
        self.department = department
    # BEHAVIOUR
    def get_student_info(self):
        print("The Student Details are:")
        print("Student:", self.sname,  "Student id:", self.sid,  "Department:", self.department)


info = college("Karthick", 9106121, "IT")
info.get_student_info()