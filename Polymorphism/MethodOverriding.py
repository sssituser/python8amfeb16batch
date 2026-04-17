class Chicken:
    def getprice(self):
        print(f'Chicken Price : Rs.260')
        
class Restaurant(Chicken):
    def getprice(self):
        print(f'Price of Chicken 65 : Rs.500')
r = Restaurant()
r.getprice()
r = Chicken()
r.getprice()
        
        