'''
Downloading the resources parallaly from the internet
'''


import threading
import time

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
# time1 = time.perf_counter()  
# #normal code    
# func(4)
# func(3)
# func(1)
# time2 = time.perf_counter()

# print(time2-time1)

#Same code using the thread

t1 = threading.Thread(target=func,args=[5])
t2 = threading.Thread(target=func,args=[2])
t3 = threading.Thread(target=func,args=[3])
t4 = threading.Thread(target=func,args=[1])
time1 = time.perf_counter() 
t1.start()
t2.start()
t3.start()
t4.start()

# below will wait for the finishing the tasks of each
t1.join()
t2.join()
t3.join()
t4.join()
time2 = time.perf_counter()

print(time2-time1)