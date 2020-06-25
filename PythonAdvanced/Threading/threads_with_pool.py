import time
from concurrent.futures import ThreadPoolExecutor

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


# With a single thread, we can do one at a time—e.g.
start = time.time()
ask_user()
complex_calculation()
print('Single thread total time: ', time.time() - start, '\n\n')


####### TWO THREADS

# With two threads, we can do them both at once...
start = time.time()

# Using with is a context manager - All this does is we don't have to call pool.shutdown()
# We can reuse threads from a pool - Do not use context manager in such a case. Create a ThreadPoolExecutor variable, wait for worker thread to finish a given task and then reuse it for another task
with ThreadPoolExecutor(max_workers=2) as pool:
	pool.submit(complex_calculation)
	pool.submit(ask_user)

print('Two thread total time: ', time.time() - start)
