#Errors can be of two types:
#1. Syntax errors: Errors caused by not following the proper structure (syntax) of the language
#Example:
testArray = [1,2,3]
print(testArray[9]) # IndexError: list index out of range
for value in testArray:
    print( value)

#2. Errors which are encountered at runtime (Exceptions): Exceptions occur during run-time
#When a Python script raises an exception, it creates an Exception object. If the script doesn't handle exception the program will terminate abruptly.

#Run-time Exception >> throw Object (Exception) >> Handled Developer/Compiler

#Python Built-in Exceptions (https://docs.python.org/3/library/exceptions.html)
#Python provides us some basic exception classes which are already defined and can be used in generic cases.
#Exception:Base class for all exceptions
#ArithmeticError:Raised when numeric calculations fails
#FloatingPointError:Raised when a floating point calculation fails
#ZeroDivisionError:Raised when division or modulo by zero takes place for all numeric types
#AssertionError:Raised when Assert statement fails
#OverflowError:Raised when result of an arithmetic operation is too large to be represented
#ImportError:Raised when the imported module is not found
#IndexError:Raised when index of a sequence is out of range
#KeyError:Raised when the specified key is not found in the dictionary
#NameError:Raised when an identifier is not found in the local or global namespace
#TypeError:Raised when a function or operation is applied to an object of incorrect type
#ValueError:Raised when a function gets argument of correct type but improper value

#Python handles exceptions using try and except blocks. In try block you can write the code which is suspicious to raise an exception,
# and in except block, you can write the code which will handle this exception.
#Keywords: try(monitor),except(Handling exceptions),else, finally,raise

# Python program to handle simple runtime error
a = [1, 2, 3]
#monitor for exceptions
try:
    print( "Second element = %d" % (a[1]))
    # Throws error since there are only 3 elements in array
    print("Fourth element = %d" % (a[3]))
#Handling the exception
except IndexError:
    print("An error occurred because the index was non-existant")

#---------------Generic Exceptions----------------
# Python program to handle simple runtime error
a = [1, 2, 3]
#monitor for exceptions
try:
    print( "Second element = %d" % (a[1]))
    # Throws error since there are only 3 elements in array
    print("Fourth element = %d" % (a[3]))
#Handling the exception
except Exception as e:
    print("Generic Exception:",e.__class__,":",e.__context__)


#Working with Built-in exceptions
print("-------Built-in exception : ArithmeticError")
try:
    a = 10/0
    print (a)
    print("Fourth element = %d" % (a[3]))
except ArithmeticError:
        print ("Arithmetic exception raised." )
#Statements to be executed only if there is no exception in your program
else:
    print ("Success.")


#Assignment: Write a user-defined function, to take in 2 integers as input and
# return the remainder of the division. Do error handling wherever possible
#Note: Operator a%b

def calculate_remainder_div(int1,int2):
    try:
        result = int(int1) % int(int2)
    except ArithmeticError:
        print ("Arithmetic exception raised." )
    else:
        return result

int1 = input("Enter integer 1: ")
int2 = input("Enter integer 2: ")

print(f"Remainder for {int1} % {int2}  is = " ,calculate_remainder_div(int1,int2))


#Assertion Error Example..Using alias names
print("-------Built-in exception : AssertionError-------")
try:
    a=10
    b=20
    assert a==b, "Value mismatch"
except AssertionError as e:
    print(e)

globals().clear()
#Example:Multiple Handlers
# A try statement can have more than one except clause, to specify handlers for different exceptions. Please note that at most one handler will be executed.
try:
    a = 5
    if a < 4:
        # throws ZeroDivisionError for a = 3
        a / (a - 3)
        # throws NameError if a >= 4
    print("Value of b = ", b) # NameError: name 'b' is not defined
# note that braces () are necessary here for multiple exceptions
#except(Exception, ZeroDivisionError, NameError) as e: - Java rule of handling more specific exception first do not apply here
except(ZeroDivisionError, NameError) as e:
    print("\nError Occurred and Handled ", e.__class__)

#Note:you can handle different exceptions all using a single block of code, they can be grouped together in a tuple
#Many exceptions are grouped into an inheritance hierarchy. For such exceptions, all of the exceptions can be caught by simply specifying a base class.
# a single except clause to handle multiple exceptions
print("-------Multiple Exceptions-------")
import errno
#import os
import logging
try:
    f = open("myFile.txt")
except OSError as e:
    if e.errno == errno.ENOENT:
        logging.error('File not found')
    elif e.errno == errno.EACCES:
        logging.error('Permission denied')
    else:
        logging.error('Unexpected error: % d', e.errno)

#Else:Else Clause:In python, you can also use else clause on try-except block which must be present after all
# the except clauses. The code enters the else block only if the try clause does not raise an exception.
# Program to depict else clause with try-except

# Function which returns a/b
def Fn_Divide(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)

# test function
Fn_Divide(2.0, 3.0)
Fn_Divide(3.0, 3.0)

# The try statement in Python can have an optional finally clause.
# This can be useful when you have clean-up activities to be done in your code
# finally is always executed
print("-------Finally Block------")
try:
   fh = open("test")
   try:
      fh.write("Test file!!")
   finally:
      print ("Closing the file")
      fh.close()
except IOError:
    print ("Error: File not found or is read-only")
finally:
    print("Inside outer finally block")

#Raising Exception: The raise statement allows the programmer to force a specific exception to occur.
# The sole argument in raise indicates the exception to be raised. This must be either an exception
# instance or an exception class (a class that derives from Exception).
try:
    raise NameError("Hi there")  # Raise Error
except NameError:  # NameError is caught
    print("An exception")
    raise  # NameError is raised

#Another Example
def example():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from e

example()

# __cause__ attribute of the exception object can be looked to follow the exception chain

try:
    example()
except RuntimeError as e:
    print("It didn't work:", e)
    if e.__cause__:
        print('Cause:', e.__cause__)
#Note:An implicit form of chained exceptions occurs when another exception gets raised inside an except block.

#Reraising the exception, that has been caught in the except block.
def example3():
    try:
        int('N/A')
    except ValueError:
        print("Didn't work")
        raise

example3()



