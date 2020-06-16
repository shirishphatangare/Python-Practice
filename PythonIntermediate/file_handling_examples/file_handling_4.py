#Other File Operations
#Tell() :This method gives you the current offset of the file pointer in a file.
#Seek() :This method can help you change the position of a file pointer in a file.
#next():Returns the next line from the last offset.
#truncate(size):Truncates the file’s size. If the optional size argument is present, the file is truncated to (at most) that size.

#Example: Python <read(size)> function to read the content of a file up to the size.
# If you don’t pass the size, then it’ll read the whole file.
file_obj = open('resources/myapplication.log', 'r', encoding = 'utf-8')
print("----------First 20 Bytes-------")
print(file_obj.read(20))    # read the first 20 characters data
position = file_obj.tell();
print('Current file position after reading 20 characters : ', position)

print("----------Read Next Lines-------")
#Reposition pointer at the beginning once again
position = file_obj.seek(0, 0);
print(file_obj.read(10))

# set the current position 6 characters to the left
print(file_obj.seek(file_obj.tell() -6))
print(file_obj.read(10))

print("----------Entire File-------")
print(file_obj.read())     # read in the rest till end of file
print("----------Reading Again-------")
print(file_obj.read())  # further reading returns empty sting


