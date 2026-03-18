li=[5,8,3,9,7,6]
print([x for x in li])
print([x*x for x in li])
print([x//2 for x in li])
sq = [x*x for x in li]
print('sq = ',sq)
halfelements =[x/2 for x in li]
print('halfelements = ',halfelements)
evens =[x for x in li if x%2==0]
print('evens = ',evens)
odds =[x for x in li if x%2 !=0]
print('odds = ',odds)