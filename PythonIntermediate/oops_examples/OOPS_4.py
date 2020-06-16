# Example : Class Account: Protecting properties using _
# protect access to the name, no, and balance attributes by prefixing these names by an underscore
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
                   '\n${}. Your withdrawal limit is {}'.format(amount, self._balance, limit)

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
act1 = Account('Douglas', 'Peterson', 3628902828)
#Error on accessing the properties
#print('first name =', act1.first_name)
print('first name =', act1._first_name)
print('first name =', act1.get_first_name())
print('last name =', act1.get_last_name())
print('account number =', act1.get_account_num())
print('account balance =', act1.get_balance())
print('deposit =', act1.deposit(1200))
print('recent transaction is:', act1.recent_transactions())
print('account balance =', act1.get_balance())
print('withdrawal =', act1.withdrawal(150))
print('recent transaction is =', act1.recent_transactions())
print('account balance =', act1.get_balance())
print('deposit =', act1.deposit(500))
print('withdrawal =', act1.withdrawal(891))
print('recent transaction is =', act1.recent_transactions())
print('withdrawal =', act1.withdrawal(49))
print('recent transaction is =', act1.recent_transactions())
