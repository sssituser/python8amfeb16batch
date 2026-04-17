import threading
import time

class Test:
    def __init__(self,name):
        self.name = name
    def player(self):
        for i in range(1,11):
            print(f'{self.name} Played {i} Time')
            time.sleep(5) # non runrable state
            
venki = Test('venki')
vijay = Test('vijay')
# unstarted state is a state in which we create object for thread class
t1 = threading.Thread(target=venki.player,name='venki') # unstarted state
t2 = threading.Thread(target=vijay.player,name = 'vijay') # unstarted state
t1.start() # Ready state is state is calling start method of a thred class
t1.join(15)
t2.start() # Ready state
