sub1 =int(input('Enter sub1 Marks : '))
sub2 =int(input('Enter sub2 Marks : '))
sub3 =int(input('Enter sub3 Marks : '))
per = (sub1+sub2+sub3)//3
if sub1>34 and sub2>34 and sub3>34:
    if per>=70:
        print("Passed in First Division")
    else:
        print("Passed in Second Division")
else:
    print("Student Failed")
