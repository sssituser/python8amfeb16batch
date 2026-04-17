class Deparatment:
    def __init__(self,did,dname,dhead,dloc):
        self.did = did
        self.dname = dname
        self.dhead = dhead
        self.dloc = dloc
    def showdepart(self):
        print(f'Depratment ID : {self.did}')
        print(f'Depratment Name : {self.dname}')
        print(f'Depratment Head : {self.dhead}')
        print(f'Depratment Location : {self.dloc}')
class Employee(Deparatment):
    def __init__(self,eid,ename,esal,did,dname,dhead,dloc):
        super().__init__(did,dname,dhead,dloc)
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def showemployee(self):
        print(f'Employee ID : {self.eid}')
        print(f'Employee  Name  : {self.ename}')
        print(f'Employee Salary :{self.esal}')
emp1 = Employee(123,"vijay Pavan",60000,111,"HR","venki","Hyd")
emp1.showemployee()
emp1.showdepart()