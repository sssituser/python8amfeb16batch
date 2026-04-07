class Student:
    def __init__(self):
        self.sid =int(input('Enter  Student ID  : '))
        self.sname =input('Enter Student Name :  ')
        self.smarks = int(input('Enter Marks'))
    def getstudent(self):
        print(f'Student ID : {self.sid}')
        print(f'Student Name  : {self.sname}')
        print(f'Student Marks  : {self.smarks}')
s1 = Student()
s1.getstudent()
        
        
s2= Student()
s2.getstudent()