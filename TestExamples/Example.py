class Employee:
    def setemployee(eid,ename,esal):
        Employee.id = eid
        Employee.name = ename
        Employee.sal = esal
    def getemployee():
        print(f'Employee ID : {Employee.id}')
        print(f'Employee Name : {Employee.name}')
        print(f'Employee Salary : {Employee.sal}')

Employee.setemployee(55,'aaa',6000)
Employee.getemployee()

Employee.setemployee(66,'ddd',7700)
Employee.getemployee()

Employee.setemployee(77,'eeee',88000)
Employee.getemployee()
Employee.getemployee()
Employee.getemployee()