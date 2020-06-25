import time
from threading import Thread

####### SINGLE THREAD

def ask_user():
	start = time.time()
	user_input = input('Enter your name: ')
	greet = f'Hello, {user_input}'
	print(greet)
	print('ask_user: ', time.time() - start)

def complex_calculation():
	print('Started calculating...')
	start = time.time()
	[x**2 for x in range(20000000)]
	print('complex_calculation: ', time.time() - start)


# With a single thread, we can do one at a time
start = time.time()
ask_user()
#complex_calculation() # Try this
complex_calculation()
print('Single thread total time: ', time.time() - start, '\n\n')


####### TWO THREADS

# With two threads, we can do them both at once...
thread1 = Thread(target=ask_user) # Try this - Execution time improvement is seen when one taks is CPU intensive task and other one is waiting for external input
#thread1 = Thread(target=complex_calculation) # Try this - Execution time improvement is NOT seen when both threads are CPU intensive tasks
thread2 = Thread(target=complex_calculation)

start = time.time()

thread1.start()
thread2.start()

# Once a thread is started don't just kill it without releasing any resources (like process specific GIL - Global interpreter Lock). Your program might run into a deadlock situationA

thread1.join()
thread2.join()

print('Two thread total time: ', time.time() - start)

