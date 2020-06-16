# Example : Class Account: List of Objects - Printing object by overrding __str__ or __repr__ methods
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

    # Overwriting the __str__ or __repr__ method to enable the instance to be printed
    # Equivalent to the toString method of Java which allows you to print the instance of a class
    def __str__(self):
        s =self.get_first_name()+' '+self.get_last_name()
        return s

    def __repr__(self):
        s = self.get_first_name() + ' ' + self.get_last_name()
        return s

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
# creating list
list = []

# appending instances to list
list.append(Account('Douglas', 'Peterson', 3628902828))
list.append(Account('Sean', 'Jefferson', 3628902827))
list.append(Account('Jeff', 'Ryan', 3628902826))

for obj in list:
    #print(obj.get_first_name(), obj.get_last_name())
    print(obj)
    #The above method will implicitly call the __str__

