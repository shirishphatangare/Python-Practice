
#Example: Here's an example of a pattern commonly seen:
def get_lines(f):
    result = []
    for line in f:
        if not line.startswith('#'):
            result.append(line)
    return result

file_obj = open("iterator_example_2.py",'r')
lines = get_lines(file_obj)
#print(lines)

#Now look at the equivalent thing as a generator:
def get_lines_gen():
    file_obj = open("iterator_example_2.py", 'r')
    for line in file_obj:
        if not line.startswith('#'):
            yield line

lines = list(get_lines_gen())

for line in lines:
    print(line)

"""
The Benefits
- Not much of a difference at first sight, but the benefits are pretty substantial.
1)No bookkeeping. You don't have to create an empty list, append to it, and return it. 
One more variable gone;
2)Hardly consumes memory. No matter how large the input file is, the generator version
 does not need to buffer the entire file in memory;
3)Works with infinite streams. The generator version still works if f is an 
infinite stream (i.e. stdin);
4)Faster results. Results can be consumed immediately, not after the entire file is read;
5)Speed. The generator version runs faster than building a list the naive way;
6) Composability. The caller gets to decide how it wants to use the result.

Generators are incredibly composable. In the example, a list is built explicitly. 
What if the caller actually needs a set? In practice, many people will either create a second,
 set-based version of the same function, or simply wrap the call in a set(). 
 Surely that works, but it is a waste of resources. Imagine the large file again. 
 First a list is built from the entire file. Then it's passed to set() to build another
  collection in memory. Then the original list is garbage collected.

With generators, the function just "emits" a stream of objects. The caller gets to decide
 into what collection those objects gets poured.
"""