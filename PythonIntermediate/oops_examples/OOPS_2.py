# Example : Class Account: Defining Functions and other properties
#1. Class variables : They are variables whose value is assigned in class
#2. Instance Variables: variables defined inside normal methods .

#Bound methods :If a function is an attribute of class and it is accessed via the instances,
# they are called bound methods. A bound method is one that has ‘self‘ as its first
# argument. Since these are dependent on the instance of classes, these are also known as
# instance methods.
class Account:
    #Class Variable
    branch='Phoenix Downtown'

    def __init__(self):
        #Instance Variables
        self.balance = 0
        print("Hello!!! We can help you manage your account")

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    # Function to withdraw the amount
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    # Function to display the amount
    def display(self):
        print("\n Net Available Balance =", self.balance)

    # # Adds an instance variable
    def setAddress(self, address):
        self.address = address
        #local variable of the method.Scope is only upto the setAddress
        branch=address

    # Retrieves instance variable
    def getAddress(self):
        return self.address

#Instantiating objects
account1 = Account()
print(account1)

# To access an object's attributes in Python, you can use the dot notation.
# This is done by typing the name of the object, followed by a dot and the attribute's name.
# Calling functions with that class object
account1.deposit()
account1.withdraw()
account1.display()
account1.setAddress("New York1, USA")
print(account1.getAddress())

# Class variables can be accessed using class name or instance
print("Class Variable using Object:",account1.branch)
print("Class Variable using class name:",Account.branch)

#Class Variable is shared across mutiple instance
account2=Account()
print("Class Variable Branch:",account2.branch)

#Here branch becomes a local variable for the instance account2.
# We can add atrributes to the instances at run-time
account2.branch="Toronto,CAN"
print("Class Variable Branch in Account1:",account1.branch)
print("Class Variable Branch in Account2:",account2.branch)
print("Class Variable using class name:",Account.branch)
#Deleting the branch attribute of account2
del(account2.branch)
print("Class Variable Branch in Account1:",account1.branch)
print("Class Variable Branch in Account2:",account2.branch)
print("Class Variable using class name:",Account.branch)
#Preferred way of changing the class variable
Account.branch="New York,USA"
print("Class Variable Branch in Account1:",account1.branch)
print("Class Variable Branch in Account2:",account2.branch)
print("Class Variable using class name:",Account.branch)