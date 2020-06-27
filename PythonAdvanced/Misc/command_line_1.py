#Python provides various ways of dealing with these types of arguments.
# The three most common are:
#1.Using sys.argv
#2.Using getopt module
#3.Using argparse module

import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
# Arguments passed
print("\nName of Python script:", sys.argv[0])
print("\nArguments passed:", end=" ")
for i in range(1, n):
    print(sys.argv[i], end=" ")

# Addition of numbers
Sum = 0
#Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
print("\n\nResult:", Sum)

#To execute this pass in the below command on terminal
#python command_line_1.py 2 3 4 5