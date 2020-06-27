#Example: reading file without Iterator

with open('iterator_example_1.py', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        else:
            print(line.rstrip())

#Rewriting the code by applying an iterator
with open('iterator_example_1.py', 'r') as f:
    print(type(f))
    f_iter = f.__iter__()
    print(type(f_iter))
    print(f.__next__()) # It indicates that f is an iterator

    for line in f: # file iterator next() method returns a new line
        print(line.rstrip())
