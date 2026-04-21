class InvalidAgeError(Exception):
    def __init__(self,message=''):
        self.message = message
        super().__init__(self.message)
        print('Invalid Age,,,,,',end="  ")
            

while True:
    try:
     age = int(input('Enter Age : '))
     if age<=0 or age>=120:
        raise InvalidAgeError("Hey Iam Custom exception")
     else:
        print(f'You haved entered age successfully,,,,,')
    except ValueError:
        print(f'Enter only numbers without decimal values')
    except InvalidAgeError as ix:
        print("Age can't be 0 or -ve and can't more or eqaul to 120",ix)
   