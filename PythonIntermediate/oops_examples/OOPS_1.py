#Object-Oriented programming is a widely used concept to write powerful applications.
# As a data scientist, you will be required to write applications to process your data,
# among a range of other things.

#Creating a class in Python
#- use the class keyword, followed by the class name and a colon.
#- Inside the class, an __init__ method is defined with def(initializer that you can later use to instantiate objects).
#  No, it is not necessary to define the __init__ in a class. A default constructor is provided by python
# --It takes one argument: self, which refers to the object itself.

# When we do not have a __init__, but still we are able to create an object
# for the class. This is because there is a default constructor implicitly injected by python

# Example : Class Account
class Account:
    pass
    # def __init__(self):
    #     pass


#Note: you have a (mostly empty) Account class, but no object yet.
#Instantiating objects
#- To instantiate an object, type the class name, followed by two brackets.
#-You can assign this to a variable to keep track of the object.

account1 = Account()
print("Type of Instance:",type(account1))


# Example : class Profile - Notice python allows multiple classes in same file without any primary class

# Python doesn’t support multiple constructors (__init__), unlike other popular object-oriented programming languages such as Java.
# We can define multiple __init__() methods but the last one will override the earlier definitions.

class Profile:
    # default constructor
    # def __init__(self):
    #     print("No Profile name is defined")

    # parameterized constructor
    def __init__(self, name="Sample_name"):
        print("Profile name is: ", name)


profile2 = Profile()
print("Type of Instance:",type(profile2))

profile1 = Profile("Shirish")
print("Type of Instance:",type(profile1))

#If we try to return a non-None value from the __init__() function, it will raise TypeError.

class Data:

    def __init__(self, i):
        self.id = i
        return True

d = Data(10)  # TypeError: __init__() should return None, not 'bool'

#If we change the return statement to return None then the code will work without any exception.


# Class with No Constructor
# We can create a class without any constructor definition.
# In this case, the superclass constructor is called to initialize the instance of the class. The object class is the base of all the classes in Python.

class SampleData:
    pass


d = SampleData()
print(type(d))


# Here is another example to confirm that the superclass constructor is called to initialize the instance of the subclass.

class BaseData:

    def __init__(self, i):
        print(f'BaseData Constructor with argument {i}')
        self.id = i


class ChildData(BaseData):
    pass


d = ChildData(10) # This behavior is different in Java
print(type(d))

#Notes:Rules regarding self.
# - Any class method must have self as first argument.
# (The name can be any valid variable name, but the name self is a widely established convention in Python.)
# - self represents an (arbitrary) instance of the class.
# -To access any class attribute inside class methods, we must prefix with self, as in self.name, where name is the name of the attribute.
# -self is dropped as argument in calls to class methods.
