#Modules in Python for filesystems
#1.os and os.path
#2.pathlib(Python 3.5)

import os
print("Current Working Directory:",os.getcwd())
myWorkingDirectory="C:/Examples/PythonSessions"
os.chdir(myWorkingDirectory)
print("Working Directory after changing:",os.getcwd())

#Scanning the current Working Directory
with os.scandir(".") as mydir:
    for entry in mydir:
        print(entry.name,entry.is_file())

#List out all the files
print("Listing of File in Current Working Directory:",os.listdir())

#Create a directory
#os.makedirs("Sample/a/b")
#os.mkdir("Sample1")

#Removing the files/directory : The directory has to be empty
os.rmdir('Sample')
#To remove non-empty directory : shutil.rmtree
#os.scandir returns an iterator whereas listdir returns a list of files/directories
#print(os.scandir("."))


import pathlib
current_path=pathlib.Path()
print("Current Working Directory:",current_path.cwd())

#Manipulating Pathname
#exists(): Checks if the file/directory structure is existing

