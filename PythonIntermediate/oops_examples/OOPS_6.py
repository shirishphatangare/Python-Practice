# Example :Fetching the list of class attributes
#It is important to know the attributes we are working with.
# For small data, it is easy to remember the names of the attributes but when
# working with huge data, it is difficult to memorize all the attributes.
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
    def get_first_name(self):
        return self._first_name


    def get_last_name(self):
        return self._last_name


    def get_account_num(self):
        return self._account_num

    def get_balance(self):
        return self._balance

#Instantiating objects and performing operations
account1 = Account('Douglas', 'Peterson', 3628902828)
# Passing both the object and class as  argument to the dir method
print("Getting properties using class object:")
print(dir(account1))
print('\nBy passing class itself ')
print(dir(Account))

print('-----Using dict--------')
#To find attributes we can also use magic method __dict__.
# This method only returns instance attributes.
# using __dict__ to access attributes
# of the object n along with their values
print(account1.__dict__)
# to only access attributes
print(account1.__dict__.keys())
# to only access values
print(account1.__dict__.values())