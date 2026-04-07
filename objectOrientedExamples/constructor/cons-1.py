class Employee:
    def __init__(self,eid,ename,esal):#constructor with Parameters
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def getemployee(self):
        print(f'Employee ID : {self.eid} ')
        print(f'Employee Name : {self.ename} ')
        print(f'Employee Salary : {self.esal} ')
        
emp1 = Employee(111,"abc",50000)
emp1.getemployee()

emp2 = Employee(222,"def",70000)
emp2.getemployee()