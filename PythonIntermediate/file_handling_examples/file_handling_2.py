#In the previous example, if an exception occurs while performing some operations on the file,
# the code exits without closing the file. So it’s better to put the code inside a <try-finally> block.

try:
   f = open('resources/myapplication.log', encoding = 'utf-8')
   # do file operations.
finally:
   f.close()

#Auto close using ‘with’
#Another way to close a file is by using the WITH clause.
# It ensures that the file gets closed when the block inside the WITH clause executes. The beauty of this method is that it doesn’t require to call the close() method explicitly.

with open('resources/myapplication.log', encoding = 'utf-8') as file_ob:
    # Display file name.
    print("File name: ", file_ob.name)
    # Display state of the file.
    print("File state: ", file_ob.closed)
    # Print the opening mode.
    print("Opening mode: ", file_ob.mode)


#<file.read(size)>:Reads the given no. of bytes. It may read less if EOF is hit.
#<file.readline(size)>:It’ll read an entire line (trailing with a new line char) from the file.
#<file.readlines(size_hint)>:It calls the <readline()> to read until EOF. It returns a list of lines read from the file. If you pass <size_hint>, then it reads lines equalling the <size_hint> bytes.