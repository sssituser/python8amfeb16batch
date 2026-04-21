while True:
    try:
        num1 = int(input('Enter num1 : '))
        num2 = int(input('Enter num2 : '))
        if num2==0:
            raise ZeroDivisionError("num2 can't be zero,,,,,,,")
        print(f'Quo : {num1/num2}')
     
    except ValueError:
        print(f'Please Enter only numbers with out decimal values')
    except ZeroDivisionError as ze:
        print(f"num2 can't be zero ",ze)
    except Exception as e :
        print('Error occured',e.__str__())
    finally:
        print('Thanku visit Again')
    
