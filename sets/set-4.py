s1 = {20,30,12,45}
s2 = {100,400,300,20}
#s3 = s1.union(s2)
s3 = s1|s2
print(s1)
print(s2)
print(s3)
s4 = s1.intersection(s2) # s4 = s1 & s3
print(s4)
#s5 = s1-s2
s5 = s1.difference(s2)
print(s5)
s6 = s2-s1  #s6 = s2.difference(s1)
print(s6)
s7 =s1^s2 #s7 = s1.symmetric_difference(s2)
print(s7)