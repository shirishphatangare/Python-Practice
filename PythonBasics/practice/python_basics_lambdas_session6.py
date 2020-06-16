#Lambda keyword in Python could be used to create anonymous functions
#Lambda expressions can be used when a function object is needed
#Note: They are restricted to a single expression

#Lamda Expressions typically have 3 parts
#1. The lambda Keyword
#2. The paramaters (or bond variables)
#3. The function Body

#Example: Lambda expression in a function

#Function to return a value added with 10
def fn_add10(a):
    return(a+10)

print (fn_add10(20))

#Simple Lambda Expression: Functional Programming
x = lambda a:a+10
print (x(6))

#Note: The lambda expression above does 3 things
#1. 'a' is considered as an argument passed to the function
#2. Performs the addition operation and return the value
#3. Implicitly called

#Example: Passing 2 arguments
x = lambda a,b:a*b
print (x(10,30))

#Example:Function returning a Lambda expression
def increment_value(x):
    return lambda m,n:m*(n+x)

#Invoking the function
inc=increment_value(30)
#inc=lambda m,n:m(n+30)
print(inc(10,2))

#Lamda with lists
numbers=[]
for x in range(5):
    numbers.append(x**2)
print (numbers)

#Alternative code using lamda using map
#Map(): Built-in function that takes a function and a sequence and applies the function on each element/item of the sequence
n=6
numbers_sq = list(map(lambda x:x**2,range(0,16,3)))
print (numbers_sq)

#Example of multiple arguments in lambda
print("------ Multiple Values in a Lambda expression----")
product= lambda x,y:x*y
print(product(10,2))
print(product(13,12))

#Example of lambda with no arguments
print("------ No Arguments in a Lambda expression----")
sample=lambda: True
print(sample())

#Example: Area of a rectangle
area_circle=lambda r: (3.14*(r**2))
print("Area of a circle with radius 5 is ",area_circle(5))

#USING LAMBDA IN MAP AND FILTER
"""
Lambda function can be used along with built-in functions like filter, map and reduce.
- Filter:takes in a function, and a list as arguments. The function return true for list element to filter them.
- Map:takes in a function and a list as argument. The function is called with a lambda function and a list and a new list is returned which contains all the lambda modified items returned by that function for each item.
- Reduce:takes in a function and a list as argument. The function is called with a lambda function and a list and a new reduced result is returned. This performs a repetitive operation over the pairs of the list.
"""
#Python map() function is used to apply a function on all the elements of specified iterable and return map object.
#an iterable item includes any of list, tuple, dictionary
#a map() function requires at least 2 positional arguments: first, a function; second, an iterable object
numerals = [1,2,3,4,5,6]
#use lambda inplace of a function
list(map(lambda value_:value_**2,numerals))
#Calculating area for a list of radius
radius=list(map(lambda r: (3.14*(r**2)),range(23,27)))
print(radius)

#Notes:The main ways lambda expressions are different from def:
#1. They can be immediately passed around (no variable needed)
#2. They can only have a single line of code within them
#3. They return automatically
#4. They can’t have a docstring and they don’t have a name

# Lambda one number arg
print('Lambda one number arg')
oneArg = lambda x: x+x*x
print(oneArg(7))
print('===========================================================')

# Lambda two numbers args
print('Lambda two numbers args')
twoArgs = lambda x, y: (x+x)*y
print(twoArgs(7, 5))
print('===========================================================')

# Lambda string
print('Lambda string')
myName = lambda name, lname: (name, lname)
callFunc = myName('Ismail', 'salmi')
print(callFunc)
print('===========================================================')

# Program to double each item in a list using map()
print('Program to double each item in a list using map')
newList = list(map(lambda x: x * 2, [1, 2, 3, 4]))
print(newList)
print('===========================================================')

# Program to add each item in a 2 lists using map
print('Program to add each item in a 2 lists using map')
inOneList = list(map(lambda x, y: x + y, [1, 2, 3], [10, 20, 30]))
print(inOneList)
print('===========================================================')

# Get even number using filter function
print('Get even number using filter function')
a = [4536,327763,3838,635,368,9215]
print(list(filter(lambda x: x % 2 == 0, a)))
print('===========================================================')

# Find item using filter on list of dicts
print('Filter list of dicts')
dict1 = {'name': 'ismail', 'age': 26}, {'name': 'yusuf', 'age': 4}
print(list(filter(lambda x: x['name'] == 'yusuf', dict1)))

print("===========================================================")
#a function that checks if the length of a name is even
def even_names(name):
    even = len(name)%2==0
    return even

#a list containing names
people = ["Joseph","Faith","Michael","Muhammed","Sandra","Israel","Victor"]

print(filter(even_names,people)) # Filter returns an iterable object which can not be printed

#using a list function to convert an iterable to the list
print(list(filter(even_names,people)))
