'''
class Name must follow Pascal Case Naming convention
'''


class Student:
    collegename = "BVRIT" # class variable or static variable
    def setstudent(self,id,name,marks):
        self.id = id # self.id is instance variable   id local variable
        self.name = name # self.name = intance variable  name is local variable
        self.marks = marks # self.marks instance variablee marks local variables
      
    def gtstudent(self):
        print("Student Info ")
        print(f'ID : {self.id}')
        print(f'Name : {self.name}')
        print(f'Marks: {self.marks}')
        print(f'College : {self.collegename}')
        
stu1 = Student()
stu1.setstudent(111,"abc",500)
stu1.gtstudent()

stu2 = Student()
stu1.setstudent(112,"def",600)
stu1.gtstudent()


    