# Receiving data through yield

from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield # Receiving data through yield
        print(f'{greeting} {friend}')

# def greet(g):
#     g.send(None) # generator priming
#     while True:
#         greeting = yield # Receiving data through yield
#         g.send(greeting)


# Another way of achieving same result
def greet(g):
    print ('Starting greet()..')
    yield from g
    print('Ending greet()..') # Note that this statement will not be reached till generator g (friend_upper()) completes

greeter = greet(friend_upper())
greeter.send(None) # generator priming
greeter.send('Hello') # Sending data to yield
print('Hello, world! Multitasking...')
greeter.send('How are you,')
