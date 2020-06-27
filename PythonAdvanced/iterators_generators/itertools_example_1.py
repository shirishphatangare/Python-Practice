#Itertools: collection of tools for handling iterators.
# Simply put, iterators are data types that can be used in a for loop.

#-The idea behind itertools is to deal with large amounts of data (typically sequence
# data sets) in a memory-efficient way.
#-All functions included in the itertools module construct and produce iterators.
# - Iterators are implementations of the iterator protocol meaning that large data sets
# can be consumed “lazily”. In other words, the whole data set does not need to be in
# memory at once during processing. Instead, each element is consumed and processed separately.
# - This eliminates common side effects of large data sets (such as swapping) leading to
# improved performance.

#Lets check this out
import operator
import time

print("--------Time Efficiency in Itertools and normal For Loop--------")

# Defining lists
L1 = [10,20,30,40,50]
L2 = [1,2,3,4,5]

# Starting time before map  function
t1 = time.time()
# Calculating result
a, b, c,d,e = map(operator.mul, L1, L2)
# Ending time after map function
t2 = time.time()
# Time taken by map function
print("Result:", a, b, c)
print("Time taken by map function: %.12f" % (t2 - t1))

# Starting time before for loop
t1 = time.time()
# Calculating result using for loop
print("Result:", end=" ")
for i in range(3):
    print(L1[i] * L2[i], end=" ")
# Ending time after for loop
t2 = time.time()
print("\nTime taken by for loop: %.12f" % (t2 - t1))

"""
The functions in the itertools module can be put into three groups:
1)Infinite iterators
2)Iterators terminating on the shortest input sequence
3)Combinatoric iterators

Infinite iterators
- Infinite iterators produce streams of infinite length (as the name suggests).
Accessing them by functions or loops to truncate the streams is strongly recommended.
There exist three of them in the itertools module: count(), cycle(), and repeat()."""

#Example of Count
#The purpose of count() is to return an iterator, that simply starts counting at a
# specified number. Optionally, you can provide the step size as a second parameter.

#infinite sequences
from itertools import count

print("----------Itertools:count------------")
#Example1:
counter = count(start=13)
print(next(counter))
print(next(counter))
print(next(counter))

print("----------Itertools:count------------")
#Second Parameter passed
counter = count(10,2)
for i in range(5):
    print(next(counter))

print("----------Itertools:count------------")
#count() can be used in combination with other functions
names = ["Alice", "Bob", "Larry", "Margaret"]
names_with_index = [name for name in zip(count(1), names)] # zip iterator returns tuples (1,'Alice'),(2,'Bob'),(3,'Larry') and so on
print(names_with_index)
#Note: zip() is a built-in function returning an iterator of tuples,
# where the i-th tuple contains the i-th element from each of the argument sequences or iterables

print("----------Itertools:Cycle------------")
#iterates over all elements of an iterable, saves a copy and returns them. Once the
# iterable is exhausted, it continues infinitely returning the saved elements.
#infinite sequences from finite sequences
from itertools import cycle

groups = cycle(['red', 'white', 'blue'])
print(next(groups))
print(next(groups))
print(next(groups))
print(next(groups))
print(next(groups))

#use case: You are teaching a class and for a group work, you want to divide the students
# into three teams. The following code snippet shows you a possible implementation of
# it using cycle()
names = ["Alice", "Bob", "Chris", "Larry", "Margaret", "Naomi", "Sarah"]
groups = cycle([1, 2, 3])
names_with_groups = [name for name in zip(names, groups)]
print(names_with_groups)

print("----------Itertools:Cycle(Finite)------------")
#finite sequences from infinite sequences
from itertools import islice
colors = cycle(['red', 'white', 'blue'])
limited = islice(colors, 0, 4)
for x in limited:
    print(x)

print("----------Repeat-------------------")
#The repeat function receives an object as parameter and returns it over and over again.
# Optionally, you can specify the number of repetitions as a second argument.
# Otherwise, it repeats forever. repeat() is commonly used together with the
# built-in map() and zip() functions.
from itertools import repeat
print (list(repeat(25, 4)))

"""
Iterators terminating on the shortest input sequence
- In contrast to infinite iterators, these functions do not produce infinite data streams. 
accumulate(): accumulate results of binary operations
chain()
chain.from_iterable()
compress()
dropwhile()
filterfalse()
groupby()
islice()
starmap()
takewhile()
tee()
zip_longest()
"""

#makes an iterator that returns the results of a function.
#accumulate results of binary operations
from itertools import accumulate
from operator import mul
numbers = [1, 2, 3, 4, 5]
#If no function is designated the items will be summed
print("----------Accumulate------------")

result1 = accumulate(numbers)
result2 = accumulate(numbers, mul)
print(f"Result 1: {list(result1)}")
print(f"Result 2: {list(result2)}")
print("---------")

#----Fetching Max values using itertools
data = [5, 2, 6, 4, 5, 9, 1]
result = accumulate(data, max)
print("Max values:",list(result))


print("---------Chain-------------")
#Used to consume multiple iterators and/or iterables sequentially instead of multiple-for loops
from itertools import chain

class1 = ["Alice", "Bob", "Chris"]
class2 = ["Larry", "Margaret", "Naomi", "Sarah"]
all_people = list(chain(class1, class2))
print(f"All people: {all_people}")

#To pass an iterable of iterators/iterables, you can use
# the alternate constructor chain.from_iterable()
all_people = list(chain.from_iterable([class1, class2]))
print(f"All people: {all_people}")

print("---------Compress-------------")
#selectively picks the values to print from the passed container according to the boolean
# list value passed as other arguments. The arguments corresponding to boolean true are
# printed else all are skipped.
# it receives two parameters:
# - data is an iterable you want to compress and
# - selectors is an iterable, which tells you whether the element in data is kept or dismissed.
from itertools import compress

def name_selection(names):
    name_selectors = []
    for name in names:
        if name.startswith("A"):
            name_selectors.append(1)
        else:
            name_selectors.append(0)
    return name_selectors

names = ["Albert", "Alexandra", "Miriam", "Sascha"]
filtered_names = list(compress(names, name_selection(names)))
print("Type of Filtered Names:",type(filtered_names))
print(f"Filtered names: {filtered_names}")
print("-------")

shapes = ['circle', 'triangle', 'square', 'pentagon']
selections = [True, False, True, False]
result = compress(shapes, selections)
for each in result:
    print(each)

print("---------Drop While & Take While-------------")
# To drop elements as long as the specified condition is true. If the condition
# once becomes false, all remaining elements are returned sequentially.
from itertools import dropwhile

print("Values Less than 5:",list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))) # Sorting of list is must for meaningful results
print ("Even Values:",list(dropwhile(lambda x : x % 2 == 0, [1, 4, 6, 4, 1])))

#returns the elements as long as the predicate is true.
from itertools import takewhile
print(list(takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])))

print("---------filterfalse()-------------")
#complement for the built-in filter() function, only returns elements in case the function returns false
from itertools import filterfalse

def is_negative(number):
    return number < 0
numbers = [-1, 0, 4, 1, -3]
positive_numbers = list(filterfalse(is_negative, numbers))
print("Positive Values:",positive_numbers)
print ("Odd Values:",list(filterfalse(lambda x : x % 2 == 0, [2, 4, 5, 7, 8])))

print("---------groupby()-------------")
#Let’s assume you have a list of data points, which consist of a group and a value.
# To make things easy, a data point is a tuple of the form (group, value), where both
# are simply integers.
from itertools import groupby
from operator import itemgetter

data = [
    (0, 0),
    (0, 1),
    (1, 4),
    (0, 9),
    (1, 2),
    (2, 5),
    (1, 6),
]
for k, v in groupby(data, itemgetter(0)):
    print(k, list(v))

#Usually, groupby() looks at the first element and appends it to the value list of the
# newly created group (with the key of the first item). If the second element’s key is
# equal to the previously used group/key, it is appended. In case it is not the same,
# a new group based on the element’s key is created, where the element is appended to
# (and so on). To get three groups (as you might have expected), we need to sort our
# data points before grouping them.

print("After Sorting-----")
data.sort()

for k, v in groupby(data, itemgetter(0)):
    print(k, list(v))

print("---Grouping Dictionary List")
robots = [{
    'name': 'blaster',
    'faction': 'autobot'
}, {
    'name': 'galvatron',
    'faction': 'decepticon'
}, {
    'name': 'jazz',
    'faction': 'autobot'
}, {
    'name': 'metroplex',
    'faction': 'autobot'
}, {
    'name': 'megatron',
    'faction': 'decepticon'
}, {
    'name': 'starcream',
    'faction': 'decepticon'
}]
for key, group in groupby(robots, key=lambda x: x['faction']):
    print(key)
    print(list(group))

#Sort the Dictionary and group it

print("-----")
sorted_robots = sorted(robots,key=lambda x: x['faction'])
for key, group in groupby(sorted_robots, key=lambda x: x['faction']):
    print(key)
    print(list(group))


print("---------isslice()-------------")

#selectively prints the values mentioned in its iterable container passed as argument.
# This iterator takes 4 arguments, iterable container, starting pos., ending position and step.
list1 = list(islice(range(50), 2))
list2 = list(islice(range(50), 40, 44))
list3 = list(islice(range(50), 5, 45, 10))

print(f"islice with stop parameter only: {list1}")
print(f"islice with start and stop: {list2}")
print(f"islice with start, stop, and step: {list3}")
print ("The sliced list values are:",list(islice([2, 4, 5, 7, 8, 10, 20], 1, 6, 2)))

print("---------starmap()-------------")
#returns an iterator that executes a given function using arguments obtained from a given iterable
#similar to the built-in map() function. However, instead of constructing a tuple from
# multiple iterators, it splits up the items in a single iterator as arguments to the
# mapping function using the * syntax.
import operator
from itertools import starmap

data = [(2, 6), (8, 4), (7, 3)]
result = starmap(operator.mul, data)
for each in result:
    print(each)

#Another Example: with a user-defined function
def pow_with_input(base, exponent):
    return base, exponent, pow(base, exponent)

values = [(4, 9), (1, 6), (0, 5), (3, 8), (2, 7)]
for i in starmap(pow_with_input, values):
    print("pow({}, {}) = {}".format(*i))


print("---------tee-------------")
# function takes an iterable and returns independent iterators based on it
# default number of returned iterators is 2, but it can be specified as the function’s second argument.
# Note:the original iterable should not be used/consumed afterwards. This may lead to unexpected behavior.
from itertools import islice
from itertools import tee

s = islice(range(100), 3)
s1, s2 = tee(s)

print(f"First list: {list(s1)}")
print(f"Second list: {list(s2)}")


print("---------zip_longest()-------------")
#the built-in zip() function to combine two iterables, it will stop if one of both is exhausted.
#to continue until the longer iterable is exhausted, you can utilize zip_longest()
# as it will fill missing values with the specified fillvalue (default is None).
from itertools import zip_longest

a = [1, 2, 3]
b = ["One", "Two"]
result1 = list(zip(a, b))
result2 = list(zip_longest(a, b))
print(result1)
print(result2)

"""
Combinatoric iterators
The group of combinatoric iterators consists of the following four functions:
- product()
- permutations()
- combinations()
- combinations_with_replacement()

"""

print("---------product()-------------")
#function computes the cartesian product for a given list of iterables
#equivalent of using nested for-loops
from itertools import product

def cartesian_product(arr1, arr2):
    # return the list of all the computed tuple
    # using the product() method
    return list(product(arr1, arr2))
arr1 = [1, 2, 3]
arr2 = [5, 6, 7]
print(cartesian_product(arr1, arr2))

#Another Example
A = [[1,2,3],[3,4,5]]
print(list(product(*A)))
#Consider 3 lists with different lengths
B = [[1,2,3],[3,4,5],[7,8]]
print(list(product(*B)))

# The difference between combinations and permutations is ordering.
# With permutations we care about the order of the elements, whereas with combinations we don’t.
print("---------permutations()-------------")
from itertools import permutations
#itertools.permutations(iterable[, r]) - Return successive r length permutations of elements in the iterable.

result1 = permutations('ABCD', 2)
for each in result1:
    print(each)

result2 = permutations(range(3)) # by default second arg is all elements in an iterable
for each in result2:
    print(each)

print("---------combinations-------------")
#function takes an iterable and a integer. This will create all the unique
# combination that have r members.
from itertools import combinations

shapes = ['circle', 'triangle', 'square']
result = combinations(shapes, 2)
for each in result:
    print(each)

print("---------combinations with replacement-------------")
#this one allows individual elements to be repeated more than once.
from itertools import combinations_with_replacement

shapes = ['circle', 'triangle', 'square']
result = combinations_with_replacement(shapes, 2)
for each in result:
    print(each)





