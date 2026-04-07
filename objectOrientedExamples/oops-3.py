class Student:
    def setstudent(self):
        print('Hi this is set student method')
    def showstudent(self):
        print('hi this is show student method')

#Note : Non static method can be accessed using object
stu = Student() # created object
stu.setstudent()
stu.showstudent()