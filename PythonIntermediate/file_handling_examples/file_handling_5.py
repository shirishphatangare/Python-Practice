#Python has the os module, which provides us with many useful methods to work with directories
# (and files as well).
import os
#Get Current Directory: getcwd() method.
print("Current Working Directory:", os.getcwd())
#use the getcwdb() method to get it as bytes object
print("Current Working Directory in Bytes:", os.getcwdb())
#Notes: The extra backslash implies escape sequence.
#List Directories and Files
print(os.listdir())
print(os.listdir('C:\\'))
#Creating a New Directory
#os.mkdir('C:\\tmp\\Hadoop')
#change the current working directory
os.chdir('C:\\tmp\\Hadoop')
print("Directory Changed:",os.getcwd())
print(os.listdir())
#Renaming a Directory or a File
os.rename('trial','new_one')
print(os.listdir())
#Removing Directory or File
#os.remove('old.txt')
#os.rmdir('new_one')
