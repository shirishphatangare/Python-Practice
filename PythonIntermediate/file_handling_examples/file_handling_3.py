#writing data to a file, first of all, open it using a mode (read/write/append)
#File Methods for writing: write()

#While writing the file, if the file does not exist, it creates a new one
with open('resources/myapplication1.log','w', encoding = 'utf-8') as file_ob:
    # first line
    file_ob.write('my first file\n')
    # second line
    file_ob.write('This file\n')
    # third line
    file_ob.write('contains three lines\n')

#Example: Reading the file line by line
#with open('C:\\temp\\myapplication1.log', 'r', encoding='utf-8') as file_ob:
#with open('C:/temp/myapplication1.log', 'r', encoding='utf-8') as file_ob:
with open('resources/myapplication1.log', 'r', encoding='utf-8') as file_ob:
    content = file_ob.readlines()
    print("Type of content:",type(content))
    for line in content:
        print(line)

#When you already have some text information in a text file and you want to append additional
# #information in it, then you can use the 'a' mode in the open function.

#<file.write(string)>: It writes a string to the file. And it doesn’t return any value.
#<file.writelines(sequence)>:Writes a sequence of strings to the file. The sequence is possibly an iterable object producing strings, typically a list of strings.