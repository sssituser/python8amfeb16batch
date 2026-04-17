import threading
import time
def player1( ):
    for i in range(1,11):
        print(f'Plyer 1 Played {i} Time')
        time.sleep(5)                                            #non runable state
        
def player2( ):
    for i in range(1,11):
        print(f'Plyer 2 Played {i} Time')
        time.sleep(5)                                            #non runable state

t1 = threading.Thread(target=player1,name='Thread-1')            #unstarted state
t2 = threading.Thread(target=player2,name='Thread-2')

t1.start()                                                      #Ready State
t1.join(10)
t2.start()
