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

#Calculating area for a list of radius
radius=list(map(lambda r: (3.14*(r**2)),range(23,27)))
print(radius)

#Notes:The main ways lambda expressions are different from def:
#1. They can be immediately passed around (no variable needed)
#2. They can only have a single line of code within them
#3. They return automatically
#4. They can’t have a docstring and they don’t have a name
#5. They use a different and unfamiliar syntax