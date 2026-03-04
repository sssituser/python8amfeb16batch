num = int(input("Enter a number : ")) #-200

if num>0 :
    if num<10:
        print(f'{num} is +ve and single digit')
    else:
        print(f'{num} is +ve but not a single digit')
else:
    print(f"{num} is not +ve")