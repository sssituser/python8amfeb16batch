t = (10,40,50,90,40)
#1.Direct elements reading
for element in t:
    print(element,end="\t")
    
#2.Reading elements using +ve index
for index in range(0,len(t)):
    print(f'\nt[{index}] => {t[index]}')
    
#3.Reading the elements using -ve index
for index in range(-len(t),0):
    print(f'\nt[{index}]=>{t[index]}')
