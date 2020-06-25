# Single-threaded task scheduler in Python

def countdown(n): # Creates a generator when this function is called
    while n > 0:
        yield n # returns 'n' and suspends execution to main thread till next() is called on this generator
        n -= 1

c = countdown(100) # generator creation
print(next(c)) # read next 'n' and give control back to the generator

tasks = [countdown(10), countdown(5), countdown(20)] # List of generators

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task) # Here task is a generator from list
        print(x)
        tasks.append(task)
    except StopIteration:  # generator do not have hasNext() method like Java to check end of generator. StopIteration exception is thrown when end of generator is reached.
        print('Task finished')

# Generators are cost effective way (compared to threads) of acheiving Python Asynchronization