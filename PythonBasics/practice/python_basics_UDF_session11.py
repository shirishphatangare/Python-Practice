#Functions in Python
#1. Built-in Functions: Python supplied functions
#2. User defined Functions

#Notes:
#Keyword def marks the start of function header.
#A function name to uniquely identify it. Function naming follows the same rules of writing identifiers in Python.
#Parameters (arguments) through which we pass values to a function. They are optional.
#A colon (:) to mark the end of function header.
#Optional documentation string (docstring) to describe what the function does.
#One or more valid python statements that make up the function body. Statements must have same indentation level (usually 4 spaces).
#An optional return statement to return a value from the function.
def greet(name):
	"""Objective: This function greets to the person passed in as parameter
		Input: Name of the person in String
		Output : Greeting the person
		Use it: greet("Name")
	"""
	print("Hello, " + name + ". Good morning!")

#Invoking the function
greet('Sean')

#Execution of function introduces a new symbol table
#Arguments are passed as call by value

#Another way to invoke the function
print(25*"-")
print ("-- Function Assigned to a variable and Invoked --")
greeting1 = greet
greeting1("Sean")

#The first string after the function header is called the docstring and is short for documentation string.
#we have a docstring immediately below the function header.
# We generally use triple quotes so that docstring can extend up to multiple lines. This string is available to us as __doc__ attribute of the function.
print(25*"-")
print ("-- Printing Function Documentation--")
print(greet.__doc__)

#Example of Returning from a function: return keyword
def absolute_value(num):
	"""This function returns the absolute
	value of the entered number"""
	if num >= 0:
		return num
	else:
		return -num

print(25*"-")
print ("-- Returning Value from Function--")
abs_value=absolute_value(2)
print(abs_value)
print(absolute_value(-4))

#Example: Returning Multiple values from a function
#Returning a list from a function
print ("-------- Returning multiple values from a function : Fibonacci Series-------")
def myFibonacci(n):
	""" Returning a list of Fibonacci series"""
	result=[]
	a,b=0,1
	while(a<n):
		result.append(a)
		a,b=b,a+b
	return result

print(myFibonacci(10))

print ("-------- Default values in a function-------")
#Example: Example Rewrite the function with default values
#Returning a list from a function
print ("-------- Returning multiple values from a function : Fibonacci Series-------")
def myFibonacci_v2(n=5):
	""" Returning a list of Fibonacci series"""
	print("Fibonacci Series of :",n)
	result=[]
	a,b=0,1
	while(a<n):
		result.append(a)
		a,b=b,a+b
	return result

print(myFibonacci_v2())
print(myFibonacci_v2(10))

print ("--------Multiple Parameter with Default values in a function-------")
#Example:
def add_values(a=5,b=0):
	return(a+b)

print("Both Parameters :",add_values(23,34))
print("Passing value for a:",add_values(34))
#Using named parameter to pass in value for the second argument
print("Passing value for b:",add_values(b=34))



print ("-------- Arbitary Argument List-------")
#Example: Providing an arbitary argument list to a function
def arithmetic_mean(first, *values):
    """ This function calculates the arithmetic mean of a non-empty
        arbitrary number of numerical values """
    return (first + sum(values)) / (1 + len(values))

print(arithmetic_mean(45,32,89,78))
print(arithmetic_mean(8989.8,78787.78,3453,78778.73))
print(arithmetic_mean(45,32))
print(arithmetic_mean(45))

#Passing only arbitary argument
def arithmetic_sum(*values):
	x=0
	x=sum(values)
	return (x)

arithmetic_sum()
arithmetic_sum(10,30,24,56)
arithmetic_sum(0,23)

print ("-------- Arbitary Argument List: Keyword Arguments-------")
#Example: Calling functions using keyword arguments
def concat_countries(*args,sep=";"):
	return sep.join(args)

#invoke the function with multiple arguments
print(concat_countries("UK","US","Phillipine","Australia","Germany","France"))
print("---Using Sep ---")
print(concat_countries("UK","US","Phillipine","Australia","Germany","France",sep=":"))

#NOtes: In a function which has variable number of arguments, the variable parameter should be defined as the last argument in the list of formal arguments
#Any argument that may oocour after the *argument has to be access as a named parameter

print ("-------- Keyword Arbitary Argument List-------")
#Arbitary Number of keyword parameters passed using **
def countries_list(**kwargs):
	print("Arguments passed using **", type(kwargs))
	print(kwargs)

countries_list(de="German",en="English",fr="French")  # Correct way
#countries_list(de:"German",en:"English",fr:"French") # Wrong way
#Would give you a TypeError if we try to pass in a list
#countries_list("UK","USA","India","Russia")

print ("-------- First Class Functions-------")
#Example: Functions passed as objects to variable
# Python program to illustrate functions can be treated as objects
def shout(text):
	return text.upper()
#print(shout('Hello'))
yell = shout
print(yell('Hello'))

print ("-------- Passing Functions as objects to other functions-------")
#Example: Functions can be passed as arguments to other functions:
def whisper(text):
	return text.lower()
def greet(func):
	# storing the function in a variable
	greeting = func("Hi, I am created by a function passed as an argument.")
	print(greeting)

greet(shout)
greet(whisper)

#Passing a function as a default argument
def greet1(text, func=whisper):
	print("Type of Argument:",type(func))
	return func(text)

print(greet1("Hello world"))
print(greet1("Hello world", shout))

#Function passed as argument in a List
def applySqr(myList, Fn_Sqr):
	result=[]
	for i in myList:
		result.append(Fn_Sqr(i))
	return result

#Calling the Function using a Built-in Function (abs)
myList=[-10,20,30,-40]
print(applySqr(myList,abs))

#Defining a Function to multiply an element by 5
def multiplyBy5(element):
	return element*5

#Multiply entire list by 5
print(applySqr(myList,multiplyBy5))

#Example: Functions can return another function:
print ("-------- Functions can return another function-------")
def create_adder(x):
	def adder(y):
		return x + y
	return adder

add_15 = create_adder(15)
print(add_15(10))

print ("-------- Default values in a function : Raise Error-------")
#Example: Passing Default Values to a function
#Example of raising/invoking an error from a function
def ask_ok(prompt,retries=4,reminder="Keep Trying..."):
	while True:
		ok=input(prompt)
		if ok in ('y','Y','yes','YES','Yes'):
			return True
		if ok in ('n','N','no','NO'):
			return False
		retries=retries-1
		if retries<=0:
			raise ValueError('Invalid Inputs')
		print(reminder)

#Invoking the function
print ("--------Only Mandatory Argument-------")
ask_ok("Do you want to continue?")
print ("--------Mandatory Argument + retries-------")
ask_ok("Do you want to continue?",2)
print ("--------All Argument-------")
ask_ok("Do you want to continue?",1,"No Tries...")
