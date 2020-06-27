#Types of Generators
#- There are two types of generators in Python:
# (1)generator functions and generator expressions.
# - A generator function is any function in which the keyword yield appears in its body.
# We just saw an example of that.
# The appearance of the keyword yield is enough to make the function a generator function.

#The other type of generators are the generator equivalent of a list comprehension.
# Its syntax is really elegant for a limited use case.

#Example: build a list of squares
numbers = [1, 2, 3, 4, 5, 6]
print("List Comprehension:",[x * x for x in numbers])
#You could do the same thing with a set comprehension:
print("Set Comprehension:",{x * x for x in numbers})
#Dictionary Comprehension
print("Dict ComprehensionL",{x: x * x for x in numbers})

print("------------------------------------")
#use a generator expression
lazy_squares = (x * x for x in numbers)
print("Type of Object:",type(lazy_squares))

# If you call __dir__ on generator object you will find that
# it contains __iter__ and __next__ methods among the other methods.
print(dir(lazy_squares))
print(next(lazy_squares))
print(next(lazy_squares))

#Generators are an incredible powerful programming construct.
# -They allow you to write streaming code with fewer intermediate variables and data
# structures.We mostly use generators for lazy evaluations. This way generators
# become a good approach to work with lots of data. If you don’t want to load all the
# data in the memory, you can use a generator which will pass you each piece of data at a time.
# -They are more memory and CPU efficient.
# -They tend to require fewer lines of code, too.

