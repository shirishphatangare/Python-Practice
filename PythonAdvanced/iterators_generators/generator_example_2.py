#Generators simplifies creation of iterators.
# Generator is a special routine that can be used to control the iteration behaviour of a loop
# similar to a function returning an array
#A generator has parameters, it can be called and it generates a sequence of numbers.
# But unlike functions, which return a whole array, a generator yields one value at a time.
#Instead, the state of the function is remembered.
# This requires less memory.
# #A generator is a function that produces a sequence of results instead of a single array/any data structure.

"""
Generators in Python:
- Are defined with the def keyword
- Use the yield keyword
- May use several yield keywords
- Return an Generator
"""

#To get a finite sequence, you call range() and evaluate it in a list context:
print("Infinite List with Iterator")

for item in range(5):
    print (item)

print("---------Generating an Infinite Sequence----------------")
print("Infinite List with Generator")
#Generating an infinite sequence, however, will require the use of a generator,
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
    print(i, end=" ")

#yield:  primary job is to control the flow of a generator function in a way that’s
# similar to return statements.
#When the Python yield statement is hit, the program suspends function execution
# and returns the yielded value to the caller. (In contrast, return stops function
# execution completely.) When a function is suspended, the state of that function is
# saved. This includes any variable bindings local to the generator,
# the instruction pointer, the internal stack, and any exception handling.
# This allows you to resume function execution whenever you call one of the generator’s
# methods. In this way, all function evaluation picks back up right after yield.

#Check out Yield Statement:
def multi_yield():
    yield_str = "This will print the first string"
    yield yield_str
    yield_str = "This will print the second string"
    yield yield_str

# Note that 2 print statements below prints same Generator object
print (multi_yield())
print(multi_yield())

gen_obj1 = multi_yield()
print(gen_obj1.__next__())
#Yield picks up right where it left
print(gen_obj1.__next__())

# Second generator object reference pointing to same generator object. But note that stack for this object will be completely a new stack
gen_obj2 = multi_yield()
print(gen_obj2.__next__())
#Yield picks up right where it left
print(gen_obj2.__next__())
print(gen_obj1.__next__()) # Gets StopIteration for gen_obj1

def yrange(n):
    i = 0
    while i < n:
        #Each time the yield statement is executed the function generates a new value.
        yield i
        i += 1


y = yrange(3)
print("Type of Object:",type(y))
print(next(y))
print(next(y))


print("------------Fibonacci series as Generators----------------------")
#Fibonacci series as Generators
from itertools import islice
def fib():
     prev, curr = 0, 1
     while True:
         yield curr
         prev, curr = curr, prev + curr

f = fib()
print(list(islice(f, 0, 10)))

#Differences from previous Code:
#- there's no return keyword inside the function body. The return value of the function
# will be a generator (read: an iterator, a factory, a stateful helper object).

#Generators can be classified as a generator function or a generator expression.
#Generator Function
print("----------Generator Function------------")
favorite_numbers = [6, 57, 4, 7, 68, 95]
def square_all(numbers):
    for n in numbers:
        yield n**2

squares = square_all(favorite_numbers)
print(list(squares))

print("----------Generator Expression------------")
#are a list comprehension-like syntax that allow us to make a generator object. not () for generator comprehension and [] for list comprehension
squares = (n**2 for n in favorite_numbers)
print(list(squares))

"""
Reading Large Files
A common use case of generators is to work with data streams or large files

def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

- The open() function returns a file object, which is an iterator object that you can lazily iterate through line by line
- You can also define a generator expression (also called a generator comprehension)
csv_gen = (row for row in open(file_name))

"""

#Profiling Generator Performance
#-Lets inspect the size of the resulting objects with sys.getsizeof()
import sys
nums_squared_lc = [i * 2 for i in range(10000)] # List comprehension returns a list
print("Without a Generator Function:",sys.getsizeof(nums_squared_lc))
nums_squared_gc = (i * 2 for i in range(10000))
print("Using a Generator Function:",sys.getsizeof(nums_squared_gc)) # Generator comprehension returns a generator

#Note: In this case, the list would be more than 10x bytes as compared to generator.
#Important: If the list is smaller than the running machine’s available memory,
# then list comprehensions can be faster to evaluate than the equivalent generator expression.
# Also If speed is an issue and memory isn’t, then a list comprehension is likely a better
# tool for the job.

#Using Advanced Generator Methods
"""In addition to next, generator objects can make use of the following methods:

.send()
.throw()
.close()

"""