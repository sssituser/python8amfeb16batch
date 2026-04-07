class Employee:
    def setemployee(self):
        self.eid = int(input('Enter Eid     : '))
        self.ename = input('Enter Ename     : ')
        self.esal = int(input('Enter Esal   : '))
    def getemployee(self):
        print(f'Employee ID : {self.eid}')
        print(f'Employee Name : {self.ename}')
        print(f'Employee Salary : {self.esal}')
       
emp1 = Employee()
emp1.setemployee()
emp1.getemployee()
