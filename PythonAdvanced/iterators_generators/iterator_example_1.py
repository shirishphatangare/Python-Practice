#Python Iterators: Iterators are objects that can be iterated upon.
#- They are implemented within for loops, comprehensions, generators etc.
#- It is simply an object that can be iterated upon.
# An object which will return data, one element at a time.
#- Python iterator object must implement two special methods, __iter__() and __next__(),
# collectively called the iterator protocol.
#- object is called iterable if we can get an iterator from it.
# Most of built-in containers in Python like: list, tuple, string etc. are iterables.

#Example: Iterating Through an Iterator in Python
#-next() function to manually iterate through all the items of an iterator.
#- If there is no more data to be returned, it will raise StopIteration
# define a list
my_list = [1,2,3,4]
# get an iterator using iter()
#The Iteration Protocol:The built-in function iter takes an iterable object and returns an iterator.
x=my_list.__iter__()
print("Type of x:",type(x))
my_iter = iter(my_list)
print("Type of Object:",type(my_iter))
## iterate through it using next()
print(next(my_iter))
print(next(my_iter))
## next(obj) is same as obj.__next__()
print(my_iter.__next__())
print(my_iter.__next__())
## This will raise error, no items left (StopIterationError)
#next(my_iter)

#We could do that using the for loop too
#internally, the for loop creates an iterator object, iter_obj by calling iter() on the iterable.

# iter_obj = iter(incoming_iterable)
# while True:
#     try:
#         print(next(iter_obj))
#         #print(iter_obj.__next__()) # This is another way of using next
#     except StopIteration:
#         print("Reached end of iterator")
#         break

"""
- Building Your Own Iterator in Python
- to implement the methods __iter__() and __next__().
 __iter__() : returns the iterator object itself. If required, some initialization can be  performed.
__next__() :must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise StopIteration.
"""

print("----------Custom Objects and Iterators-------------")
#Example: Custom Objects and Iterators
# build your own iterator using __iter__ and __next__ methods.
class SquareOfNumbers:
    """Class to implement an iterator
    of powers of two"""
    def __init__(self, max = 0):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

a = SquareOfNumbers(4)
i = iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))

"""
Iterators have several advantages:
1)Cleaner code
2)Iterators can work with infinite sequences
3)Iterators save resources:when working with iterators, we can get the next element
 in a sequence without keeping the entire dataset in memory.
"""

print("----------Custom Objects and Iterators(Fibonacci numbers)-------------")
#Example:iterator producing the Fibonacci numbers:
from itertools import islice
class fib:
     def __init__(self):
         self.prev = 0
         self.curr = 1
     def __iter__(self):
        return self
     def __next__(self):
         value = self.curr
         self.curr += self.prev
         self.prev = value
         return value
f = fib()
#islice: Converts into an iterator
print(list(islice(f, 0, 10))) # Converting into a list for printing
print(next(f))
print(next(f))
print(next(f))

print("----------Custom Objects and Iterators(Sequence)-------------")
#Another Iterator
class Seq:
    def __init__(self):
        self.x = 0
    def __next__(self):
        self.x += 1
        return self.x ** self.x
    def __iter__(self):
        return self
s = Seq()
n = 0
for e in s:
    print(e)
    n += 1
    if n > 10:
        break

# Trying iter() with sentinel
def iter_seq_inifinite():
    for e in s:
        return e

#inf = iter(iter_seq_inifinite, 5)
# Below loop will go in infinite loop
# for e in inf:
#     print(e)

# To fix infinite loop issue create an iterator with right sentinel value

inf = iter(iter_seq_inifinite, 3125) # sentinel (3125) exclusive
#Infinite iterator fixed by using iter(iter_seq_inifinite, 3125) with right sentinel value - 3125
for e in inf:
    print(e)

"""
Assignment: 
1. Modify the Above Custom Iterator to interrupt the loop after 10 iterations
2. Write an iterator class reverse_iter, that takes a list and iterates it from the 
reverse direction.

Solutions are below - 
"""
# Custom Iterator to interrupt the loop after 10 iterations
class Seq_max_10:
    def __init__(self):
        self.x = 0
    def __next__(self):
        self.x += 1
        if self.x > self.max:
            raise StopIteration
        else:
            return self.x ** self.x
    def __iter__(self):
        self.max = 10
        return self

s = Seq_max_10()
n = 0
# for loop internally handles StopIteration
for e in s:
    print(e)
    n += 1

# Iterator to reverse a list
class Reverse_list:
    def __init__(self, my_list):
        self.cur_index = 0
        self.my_list = my_list

    def __next__(self):
        self.cur_index -= 1
        return self.my_list[self.cur_index]

    def __iter__(self):
        return self

my_list = [1,2,3,4,5]
my_rev_iter = Reverse_list(my_list)

print(my_rev_iter.__next__())
print(my_rev_iter.__next__())
print(my_rev_iter.__next__())


'''
Lets explore some concepts in Python:
- a container
- an iterable
- an iterator
- a generator
- a generator expression
- a {list, set, dict} comprehension

Containers
- Containers are data structures holding elements, and that support membership tests.
- They are data structures that live in memory, and typically hold all their values in memory,
- E.g of Containers: list, deque,set, frozensets,dict, defaultdict, OrderedDict,tuple, namedtuple, …
- Containers are easy to grasp, because you can think of them as real life containers:
  a box, a cubboard, a house, a ship, etc.
- an object is a container when it can be asked whether it contains a certain element.

Iterables
- most containers are also iterable. But many more things are iterable as well.
- Examples are open files, open sockets, etc. Where containers are typically finite,
an iterable may just as well represent an infinite source of data.
- An iterable is any object, not necessarily a data structure, that can return an iterator
 (with the purpose of returning all of its elements). It has __iter__() method to return an iterator

Iterators
- It's a stateful helper object that will produce the next value when you call next() on it.
- Any object that has a __next__() method is therefore an iterator. How it produces a value
is irrelevant.
- So an iterator is a value factory. Each time you ask it for "the next" value, it knows
 how to compute it because it holds internal state.
- There are countless examples of iterators. All of the itertools functions return iterators.
 Some produce infinite sequences:
 - Itertools(Functions creating Iterators):https://docs.python.org/3/library/itertools.html

Generators
- A generator is a special kind of iterator

'''