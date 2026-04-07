class Employee:
    def setemployee(): # static methods
        print('Hi this is set employee method')
        
    def showemployee(): #static method
        print('Hi this is show emplyee method')
        
# emp1 = Employee() # object creation
# emp1.setemployee()
# emp1.showemployee()
#NOTE : Static methods can be called using class name
Employee.setemployee()
Employee.showemployee()