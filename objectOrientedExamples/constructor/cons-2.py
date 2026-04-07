class Employee:
    eid :int
    ename : str
    esal :int #Static variables
    def __init__(self): # constructor without paramter
        Employee.eid = int(input('Enter Employee ID : '))
        Employee.ename = input("Enter Name : ")
        Employee.esal = int(input('Enter Salary : '))
    def getemployee(self):
        print(f'Employee ID : {Employee.eid}')
        print(f'Employee Name :{Employee.ename} ')
        print(f'Employee Salary : {Employee.esal}')
emp1 =Employee()
emp1.getemployee()