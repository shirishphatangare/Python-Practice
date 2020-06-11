#Module Programming in Python is supported by two mechanisms:
#1. Modules
#2. Packages

#A module is a single file (or files) that are imported under one import and used.
#A package is a collection of modules in directories

#There are actually three different ways to define a module in Python:
#1. A module can be written in Python itself.
#2. A module can be written in C and loaded dynamically at run-time, like the re (regular expression) module.
#3. A built-in module is intrinsically contained in the interpreter, like the itertools module.

#A module’s contents are accessed the same way in all three cases: with the import statement.

# Python Module example
def add(a,b):
   """This program adds two numbers and return the result"""
   result = a + b
   return result

def sub(a, b):
   """This program subtracts two numbers and return the result"""
   result = a - b
   return result

def multiply(a, b):
   """This program multiplies two numbers and return the result:multiply(a, b)"""
   result = a * b
   return result

def addMultiple(*args):
   return (sum(args))

# Define a variable
addittive_identity=0
multiplicative_identity=1

if __name__ == "__main__":
    print("****Add Function:",add(12,34))

print("----------Module Saved----------")

#Modules are often designed with the capability to run as a standalone script for purposes
# of testing the functionality that is contained within the module.
# This is referred to as unit testing.

#if a file is run as a standalone script, __name__ is (creatively) set to the string '__main__