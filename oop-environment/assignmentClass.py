from __future__ import print_function

class College:
    def __init__(self):
        self.collegeName = "Khwopa Engineering College"


class Faculty(College):
    def __init__(self,facName):
        self.facultyName = facName
        College.__init__(self)

class Teacher(Faculty):
    def __init__(self,name,period,salary,facName):
        self.name = name
        self.period = period
        self.salary = salary
        Faculty.__init__(self,facName)


class Student(Faculty):
    def __init__(self,name,sub,mark,fac):
        self.name = name
        self.subject = sub
        self.mark = mark
        Faculty.__init__(self,fac)

    def result(self):

        if self.mark >= 80:
            res = "Excellent"
        elif self.mark >= 60:
            res = "Good"
        elif self.mark >= 40:
            res = "Satisfactory"
        else:
            res = "Not Good"
        print(self.name,"result is",res,"in",self.subject)



teacher1 = Teacher("Boss",2,80000,"Computer")
print(teacher1.name,"is a teacher in",teacher1.collegeName,"who teaches",teacher1.period,"periods in",teacher1.facultyName,"Department and have a salary of Nrs.",teacher1.salary)

student1 = Student("Good Student","Physics",55,"Computer")
print(student1.name,"is studying in",student1.collegeName,"in",student1.facultyName," faculty has scored",student1.mark,"in",student1.subject)
student1.result()