
#To Get started
#1. Python software : Version 3
#2. Editor : PyCharm, Jupyter Notebook

#Python Documentation: https://docs.python.org/3/library/index.html

#This is a comment in Python - Single Line Comment

# print examples
print("Hello World");
# You could pass multiple arguments to the print statement
print ("Hello World", "Welcome to Python");
#Arguments could be of different types
print ("Hello World", "Welcome to Python",3.14,2020);
#By default the delimiter is space but you could specify a new delimiter by using attribute as 'sep'
print ("Hello World", "Welcome to Python",3.14,2020,sep=":")

#Variable Declaration : Python is not a strongly/statically typed language and so no datatype - It is a dynamic typed language
#Python variables : No datatypes and takes in the type of the data which is passed to it
#Variable declaration and assignment happens together.
myint = 7
print(myint)
#Check on the type of the variable
print(type(myint))

#Different Categories of Data Types in Python
#1. Scalar Types : Numbers, Booleans, Strings (Class) : Holds only 1 value
#2. Complex Types: Lists,Sets, Dictionaries : Hold multiple values

#Assignments can be done on more than one variable "simultaneously"
a, b = 3, 4
print(a,b)

a,b,c = 30,"UK",10.5
print(a,b,c)

a,b,c = 30,"UK" # Statement results in a Value Error
print(a,b,c)

#Floating Point values
myfloat = 7.023
print(myfloat)

#Type casting can be done by using certain functions
myint = int(myfloat)
print(myint)

myfloat = float(7)
print(myfloat)

#Reading value of a variable at run time: input()
today_date=input("Whats the date today?")
print(type(today_date))
#Usually the input method returns a string value
#Use the appropriate type casting functions like int(),float() to convert it into the data type of your choice

print("Todays Date is :",today_date)
#print("Tommorrows Date:",(today_date+1)) # TypeError: can only concatenate str (not "int") to str
print("Tommorrows Date:",int(today_date) + 1) # Success 1 - int addition
print("Tommorrows Date:",(today_date + str(1))) # Success 2 - String concatenation

#Defining Strings
mystring = 'hello'
print(mystring)

mystring = "hello"
print(mystring)

#You could use \ as an escape sequence
print("Learning \"Python\" is easy..Isn't it?")
print('Learning "Python" is easy..Isn\'t it?')
#Double Quotes retain quotes
mystring = "Don't worry about apostrophes"
print(mystring)

print('C:\SomeFile\newfile');
#Using raw string: Used to ignore the special characters like '\n' here
print(r'C:\SomeFile\newfile');
#or
print('C:\SomeFile\\newfile');
sample=r'C:\SomeFile\newfile'
print(sample);

#Printing String along with variables
name="Atos Syntel"
print("Welcome to ",name, ".....")
year=2020
print("The current year is:",year)


#Spanning Multiple Lines using """ to retain formatting
print("""
    Hello
        Welcome to print Statement
    This String spans multiple line 
""")

#Operators
#Arithmetic : +,-,*,/,%,**
x = 3
y = 2.0
print(x+y)
print(x-y)
print(x*y)
print(x/y)
# ** -> Power, % - Remainder
print(2**3);
print(3%2);
# // --> Floor of quotient value
print(3//2)

#String Operators
#1. +(Concatenation)
#2. *(Repetition)

#Strings are immutable in Python. Concating creates a new string
#String concatenation (+)
str1="Atos";
str2=" Syntel" # semicolons are optional at the end
year=2020

str3=":"
#print(str1+str2+str3+year) # TypeError
print(str1+str2+str3,year) # success

#String Repetition (*)
print(3*"hello...");
print(3*(str1+str2));
print((str1+str2)*3);

#Strings are array of bytes in Python and hence the array values can be
# extracted using index poisition you could also do indexing in Strings
#indexing in Python: starts with 0
#Strings can be indexed in Python. String indexes start with 0
str1="PythonProgramming"
#Left to Right index starts with 0. Right to Left index starts with -1
print(str1[0]);
#Negative string indexes help start returniing characters from right to left
print(str1[-3]);
print(str1[-6]);

# If the index positions are out of range you get an IndexError
#print(str1[-26]);

#Slicing of Strings
print(str1[2:5]) #slicing the string starting fronm index poistion 2 upto 4(5 is not included in the slice)
print(str1[2:]) #Slicing from index position 2 upto the end of the string
print(str1[:6]) #Slicing from beginning upto the position 5
print(str1[-2:]) #Slicing from position -2
print(str1[:-2]) #Slicing till position -2

#operators between numbers and strings is not supported
# This will not work! Error - TypeError
one = 1
two = 2
hello = "hello"
#print(one + two + hello)

#Python strings are immutable
#str3[0]='J' # str3 is already defined above and we can not change String as this statement - TypeError: 'str' object does not support item assignment

str5 = "Dummy"
#We could create a new string
str4 = 'J'+str5[:]
print(str4)

#String is immutable and cant be changed once created
str3="Python"
#str3[0]="J"
print(str3)

str3="Atos"
#str3[0]='P'
print(str3)

#We could create a new string
str4 = 'J'+str3[1:]
print(str4)

#Explore all the functions in str
dir(str)
#Explore the other string functions: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
#Some String Functions
print("Length(len):",len(str3));

time.sleep(15)


