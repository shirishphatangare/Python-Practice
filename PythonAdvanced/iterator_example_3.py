# Infinite Iterators
# -There can be infinite iterators (which never ends).
# We must be careful when handling such iterator.

# built-in function iter() can be called with two arguments where the first argument must
# be a callable object (function) and second is the sentinel. The iterator calls this
# function until the returned value is equal to the sentinel.
print(int())
inf = iter(int, 1)
print(next(inf))
print(next(inf))
print(next(inf))

# Note:We can see that the int() function always returns 0. So passing it as iter(int,1)
# will return an iterator that calls int() until the returned value equals 1.
# This never happens and we get an infinite iterator.

# Custom Infinite Iterators

"""
Why are iterators a good idea?
 - Code using iterators can avoid intermediate variables, lead to shorter code, 
 run lazily, consume less memory, run faster, are composable, and are more beautiful. 

 In short: they are more elegant.

 - As soon as something's iterable, you can feed it to list(), set(), sorted(), min(),
  max(), heapify(), sum(), ‥. Many of the tools in Python consume iterators."
"""
