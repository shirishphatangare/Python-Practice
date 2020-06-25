#Threading as a sub-class
import threading as th
import time

class SubclassThread(th.Thread):

   def __init__(self, name, delay):
      th.Thread.__init__(self)
      self.name = name
      self.delay = delay

   def thread_delay(self,thread_name, delay):
      count = 0
      while count < 3:
         time.sleep(delay)
         count += 1
         print(thread_name, '-------->', time.time())

   def run(self):
      print('Starting Thread:', self.name)
      self.thread_delay(self.name, self.delay)
      print('Execution of Thread:', self.name, 'is complete!')


t1 = SubclassThread('t1', 1)
t2 = SubclassThread('t2', 3)
#t2 = SubclassThread('t2', 0.5)

t1.start()
t2.start()

# Below joins do not guarantee that t2 completion will follow t1 completion. but guarntees that main will continue execution only after t1 and t2 finishes
t1.join()
t2.join()

print("Thread execution is complete!")
