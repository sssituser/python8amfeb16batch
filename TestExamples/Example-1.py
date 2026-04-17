class Employe:
    def setempmloyee(self,eid,ename,esal):
        self.id = eid
        self.name = ename
        self.sal = esal
    def getemployee(self):
        print(f'Employee ID : {self.id}')
        print(f'Employee Name : {self.name}')
        print(f'Employee Salary : {self.sal}')
emp1 = Employe()
emp1.setempmloyee(111,'vijay',50000)
emp1.getemployee()

emp2 = Employe()
emp2.setempmloyee(112,'venky',50000)
emp2.getemployee()

emp3 = Employe()
emp3.setempmloyee(113,'Pavan',50000)
emp1.getemployee()
emp2.getemployee()
emp3.getemployee()