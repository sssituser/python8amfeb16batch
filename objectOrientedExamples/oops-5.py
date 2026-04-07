class Employee:
    def setemployee(self,eid,ename,esal):
        print('Hi Iam Set Employee Mehod')
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def getemployee(self):
        print(f'Employee ID     : {self.eid}')
        print(f'Employee Name   : {self.ename}')
        print(f'Employee Salary : {self.esal}')
        
emp1 = Employee()  #Creation of object
emp1.setemployee(111,"abc",50000)
emp1.getemployee()
        
emp2 = Employee()  #Creation of object
emp2.setemployee(112,"def",60000)
emp2.getemployee()