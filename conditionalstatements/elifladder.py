sub1 =int(input('Enter sub1 Marks : '))
sub2 =int(input('Enter sub2 Marks : '))
sub3 =int(input('Enter sub3 Marks : '))
per = (sub1+sub2+sub3)/3
if sub1<35 or sub2<35 or sub3<35:
    print("Student Failed")
elif per>=70:
    print(f"Passed Distinction with the percentage of :{per}")
elif per>=60:
    print(f"Passed First Division with the percentage of :{per}")
elif per>=50:
    print(f"Passed Second Division with the percentage of :{per}")
else:
    print(f"Passed Third with the percentage of :{per}")

    