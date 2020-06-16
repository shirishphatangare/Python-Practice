# There are three types of methods in Python:
# instance methods, static methods, and class methods.
#1. Instance Methods: The most common method type. Able to access data and properties unique
# to each instance.
#2. Static Methods: Cannot access anything else in the class. Totally self-contained code.
#3. Class Methods: Can access limited methods in the class. Can modify class specific details.

#static method is bound to a class rather than the objects for that class
#This means that a static method can be called without an object for that class.
# This also means that static methods cannot modify the state of an object as they are not bound to it.

# use-case. When we need some functionality not w.r.t an Object but w.r.t the complete class,
# we make a method static. This is pretty much advantageous when we need to create Utility methods as
# they aren’t tied to an object lifecycle usually.

#2 Approaches to deal with statis methods:1. staticmethod() and 2.@staticmethod

class Account:
    # All variables which are assigned a value in class declaration are class variables
    Acc_count=0

    def __init__(self, first_name, last_name, account_num, balance=0):
        self._first_name = first_name
        self._last_name = last_name
        self._account_num = account_num
        self._balance = balance
        self._transactions = []
        #increment the count everytime an instance is created
        Account.Acc_count += 1

    #Creating the static method to keep a count of accounts
    @staticmethod
    def accountCount():
        return Account.Acc_count

    def deposit(self, amount):
        self._balance += amount
        #keeping a track of the transactions
        self._transactions.append(+amount)
        return amount

    # Function to withdraw the amount(caps the daily withdrawal to $500)
    def withdrawal(self, amount, limit=500):
        if self._balance - amount > 0 and amount <= limit:
            self._balance -= amount
            self._transactions.append(-amount)
            return amount
        else:
            return 'Your withdrawal amount is ${} which exceeds your account limit! You have:' \
                   '\n${}. Your withdrawal limit is {}'.format(amount, self._balance, limit)

    # Function to display the amount
    def display(self):
        print("\n Net Available Balance =", self._balance)

    # Function recent_transactions() method that returns the most recent transaction.
    def recent_transactions(self):
        if len(self._transactions) < 1:
            return None
        else:
            return self._transactions.pop()

    #Some additional Getter methods
    #A method which is used for getting a value is decorated with "@property"
    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    #The method which has to function as the setter is decorated with "@x.setter"
    @first_name.setter
    def first_name(self,first_name):
        self._first_name=first_name

    def get_account_num(self):
        return self._account_num

    def get_balance(self):
        return self._balance

#Instantiating objects and performing operations
account1 = Account('Abby', 'Peterson', 3628902828)
account2 = Account('Sam', 'Jackson', 3628902828)
account3 = Account('Sean', 'Billy', 3628902828)

#Getting the count of instance
print("No of Instances:",Account.accountCount())
print("No of Instances:",account1.accountCount())

#trying to change the variable value from an instance
print("After changing the value of variable using an Object")
account1.Acc_count=45
print("No of Instances:(Account1) - variable access",account1.Acc_count)
print("No of Instances:(Account1) - static Method access",account1.accountCount())
print("No of Instances:(Account2)",account2.Acc_count)
print("No of Instances:(Account Class)",Account.accountCount())
