#Decorators are design patterns in Python.They apply logic or change the behavior
# of other functions. They are an excellent way to reuse code, and can help to
# separate logic into individual concerns.
#1.@property decorator; a pythonic way to use getters and setters in object-oriented programming.

#Why is it needed?
# (1) We can make objects out of this class and manipulate the attribute as we wish.To prevent
# this we try to define the variables using _ to protect them.As you know The private
# variables don't actually exist in Python. There are simply norms to be followed.
# The language itself doesn't apply any restrictions.
# To update those we create getters and setters and during a refactoring, it cause problems
# while dealing with hundreds of thousands of lines of codes.This is where @property is use

class Account:
    def __init__(self, first_name, last_name, account_num, balance=0):
        self._first_name = first_name
        self._last_name = last_name
        self._account_num = account_num
        self._balance = balance
        self._transactions = []

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
                   '\n${}. Your withdrawal limit is {}'.format(amount, self.balance, limit)

    # Functin to display the amount
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
        if(len(first_name)<=1):
            raise ValueError("First Name cannot be less than a character")
        self._first_name=first_name

    def get_account_num(self):
        return self._account_num

    def get_balance(self):
        return self._balance

#Instantiating objects and performing operations
account1 = Account('Douglas', 'Peterson', 3628902828)
#Setting the New Value
account1.first_name="Dan"
print("First Name:",account1.first_name)
account1.first_name="J"
print("Last Name:",account1.last_name)

