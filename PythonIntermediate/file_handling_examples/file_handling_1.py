#File handling is nothing but a combination of various operations performed on the files
# such as opening the file, reading the file, and writing the file, etc.

#Reference: https://docs.python.org/2.4/lib/bltin-file-objects.html

#There are generally two types of files — text file and binary file.
#1. Text File: A text file stores the textual information and saved as .txt extension,
# 2. Binary File: Images are stored in the form of binary numbers such as 0’s or 1’s and saved as .bin extension.
#(binary :b)

#In Python, file processing takes place in the following order.
#1.Open a file that returns a filehandle.
#2.Use the handle to perform read or write action.
#3.Close the filehandle.

#1. Opening the File
# - use its in-built open() function which returns a file object, i.e., a handle.
# - Syntax: file object = open(file_name [, access_mode][, buffering])
# - access_mode:file opening mode, e.g., read, write, append, etc. (optional parameter).
#  By default, it is set to read-only <r>.

#File Attributes
#<file.closed>	For a closed file, it returns true whereas false otherwise.
#<file.mode>	It returns the access mode used to open a file.
#<file.name>	Returns the name of a file
#<file.softspace>	It returns a boolean to suggest if a space char will get added before printing another value in the output of a <print> command.

#Example: Open a file in read mode and check out on the properties.
file_ob = open("resources/myapplication.log", "r")

#Display file name.
print("File name: ", file_ob.name)
#Display state of the file.
print("File state: ", file_ob.closed)
#Print the opening mode.
print("Opening mode: ", file_ob.mode)
#Closing the File
file_ob.close()

#Note: It’s always the best practice to close a file when your work gets finished.
# However, Python runs a garbage collector to clean up the unused objects.Its a good practice to do it on your own

#Other Modes:
#<rb>	It opens a file in (binary + read-only) modes. And the offset remains at the root level.
#<r+>	It opens the file in both (read + write) modes while the file offset is again at the root level.
#<rb+>	It opens the file in (read + write + binary) modes. The file offset is again at the root level.
#<w>	It allows write-level access to a file. If the file already exists, then it’ll get overwritten. It’ll create a new file if the same doesn’t exist.
#<wb>	Use it to open a file for writing in binary format. Same behavior as for write-only mode.
#<w+>	It opens a file in both (read + write) modes. Same behavior as for write-only mode.
#<wb+>	It opens a file in (read + write + binary) modes. Same behavior as for write-only mode.
#<a>	It opens the file in append mode. The offset goes to the end of the file. If the file doesn’t exist, then it gets created.
#<ab>	It opens a file in (append + binary) modes. Same behavior as for append mode.
#<a+>	It opens a file in (append + read) modes. Same behavior as for append mode.
#<ab+>	It opens a file in (append + read + binary) modes. Same behavior as for append mode.

#Python File encoding
#  Python stores a file in the form of bytes on the disk, so you need to decode them in strings before reading.
#  And, similarly, encode them while writing texts to the file.
#  Python enables platform-dependent encoding by default(if you don’t change it, then it’s set to <cp1252> for Windows and <utf-8> for Linux.)
# to quote the desired encoding while opening a file in Python.
# f = open('myapplication.log', mode = 'r', encoding = 'utf-8')