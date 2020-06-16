# Example : Class Account: Adding other properties
class Account:

    def __init__(self, first_name, last_name, account_num, balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.account_num = account_num
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        #keeping a track of the transactions
        self.transactions.append(+amount)
        return amount

    # Function to withdraw the amount(caps the daily withdrawal to $500)
    def withdrawal(self, amount, limit=500):
        if self.balance - amount > 0 and amount <= limit:
            self.balance -= amount
            self.transactions.append(-amount)
            return amount
        else:
            return 'Your withdrawal amount is ${} which exceeds your account limit! You have:' \
                   '\n${}. Your withdrawal limit is {}'.format(amount, self.balance, limit)

    # Function to display the amount
    def display(self):
        print("\n Net Available Balance =", self.balance)

    # Function recent_transactions() method that returns the most recent transaction.
    def recent_transactions(self):
        if len(self.transactions) < 1:
            return None
        else:
            return self.transactions.pop()

#Instantiating objects and performing operations
act1 = Account('Douglas', 'Peterson', 3628902828)
print('first name =', act1.first_name)
print('last name =', act1.last_name)
print('account number =', act1.account_num)
print('account balance =', act1.balance)
print('deposit =', act1.deposit(1200))
print('recent transaction is:', act1.recent_transactions())
print('account balance =', act1.balance)
print('withdrawal =', act1.withdrawal(150))
print('recent transaction is =', act1.recent_transactions())
print('account balance =', act1.balance)
print('deposit =', act1.deposit(500))
print('withdrawal =', act1.withdrawal(891))
print('recent transaction is =', act1.recent_transactions())
print('withdrawal =', act1.withdrawal(49))
print('recent transaction is =', act1.recent_transactions())
