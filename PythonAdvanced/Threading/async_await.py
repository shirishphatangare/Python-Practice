from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

# A coroutine is a function which co-executes with other coroutines simultaneously. A coroutine can pause and resume its execution.
@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield # yielding control to receive input from amother coroutine
        print(f'{greeting} {friend}')

# Function becomes a coroutine with keyword - async
async def greet(g):
    print('Starting...')
    # await <awaitable_object> - awaitable_objects are : coroutines, Tasks, and Futures
    await g  # Pause an execution of current coroutine (greet()) on another coroutine (here friend_upper())
    print('Ending...') # This statement is executed only after friend_upper() coroutine completes its execution

greeter = greet(friend_upper())
print(type(greeter)) # Getting back a coroutine Object
greeter.send(None)
greeter.send('Hello')

greeting = input('Enter a greeting: ')
greeter.send(greeting)

greeting = input('Enter a greeting: ')
greeter.send(greeting)
