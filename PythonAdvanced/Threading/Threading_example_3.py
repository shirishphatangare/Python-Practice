#Find the active threads

import threading
import time

def fun1(a, b):
   #Comment below line after the first execution to see the change in active thread count
   time.sleep(1)
   c = a + b
   print(c)

thread1 = threading.Thread(target = fun1, args = (12, 10))
thread1.start()

thread2 = threading.Thread(target = fun1, args = (10, 17))
thread2.start() # output showing as 2722 is actually 27 from second thread and 22 from first thread printing simultaneously
print("Total number of threads", threading.activeCount())
