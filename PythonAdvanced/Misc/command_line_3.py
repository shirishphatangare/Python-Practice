#The Python argparse library was released as part of the standard library with Python 3.2
# Lets understand about arguments, options, and parameters,terminology :
# 1. An argument is a single part of a command line, delimited by blanks.
# 2. An option is a particular type of argument (or a part of an argument) that can modify the behavior of the command line.
# 3. A parameter is a particular type of argument that provides additional information to a single option or command.

#Example: ls -l /var/log
#In this example, you have different arguments:
#ls: the name of the command you are executing
#-l: an option to enable the long list format
#/var/log: a parameter that provides additional information (the path to list) to the command

#The argparse module makes it easy to write user-friendly command-line interfaces.
# It parses the defined arguments from the sys.argv.
#The argparse module also automatically generates help and usage messages, and
# issues errors when users give the program invalid arguments.
#The argparse is a standard module; we do not need to install it.
#A parser is created with ArgumentParser and a new parameter is added with add_argument().
# Arguments can be optional, required, or positional.

#Using the Python argparse library has four steps:
#1.Import the Python argparse library
#2.Create the parser
#3.Add optional and positional arguments to the parser
#4.Execute .parse_args()

import argparse
import datetime

# help flag provides flag help
# store_true actions stores argument as True
import random
# Try different commented options below
parser = argparse.ArgumentParser()
#The action set to store_true will store the argument as True, if present.
parser.add_argument('-o', '--output', action='store_true',help="shows output")

#---Adding a Required Argument
parser.add_argument('--name', required=True)

#Working with Positional Arguments
#parser.add_argument('name')
#parser.add_argument('age')

#Giving a Name to the argument
parser.add_argument('-n', dest='now', action='store_true', help="shows now")

#Defining the Type of Argument
#parser.add_argument('-n', type=int, required=True, help="define the number of random integers")

#Looking for Arguments
args = parser.parse_args()
#parse_args() returns a Namespace object that contains a simple property for each
# input argument received from the command line.

if args.output:
    print("This is some output")
if args.name:
    print(f'Hello {args.name}')

#For positional Arguments
#print(f'{args.name} is {args.age} years old')

#New Argument Name
if args.now:
    now = datetime.datetime.now()
    print(f"Now: {now}")

#n = args.n
#Checking on Type of Arguments
#for i in range(n):
#    print(random.randint(-100, 100))

#Excute the code on Command Line Terminal
#Optional Arguments
#1. python command_line_3.py --help
#2. python command_line_3.py --output or python ArgParse3.py -o

#Required Arguments
#1. python command_line_3.py --name Peterson

#Positional Arguments
#python command_line_3.py Nancy 3

#Giving an argument a name
#python command_line_3.py -n

#Type of argument
#python command_line_3.py -n 3