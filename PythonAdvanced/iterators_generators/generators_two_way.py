from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

# Yielding from another iterator
def get_friend():
    yield from friends # get_friend() is a generator but yielding values from global iterator


def greet(g):
    while True:
        try:
            friend = next(g) # Calling Generator 1 next()
            yield f'HELLO {friend}'
        except StopIteration:
            pass


friends_generator = get_friend() # Generator 1
g = greet(friends_generator) # Generator 2

print(next(g))  # Calling Generator 2 next()
print(next(g))

