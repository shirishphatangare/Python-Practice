"""
1. Create a Checking Accounts Class and derive it from Account Class
- deposit() : Any amount can be deposited
- withdraw() : Maximum 6 withdrawals are permitted per month. Withdraw amount should be at the most 700$

2. Create a Savings Account Class and derive it from Account Class
- deposit() : Any amount can be deposited
- withdraw() : Unlimited withdrawals are permitted.

3. Modify the Account class to accept the properties of Account holder
like the firstname,lastname and address from a different Class named as AccountHolder

Create 3 instances of Account. Each of the instances will have both Checking and Savings account
Main all the transactions done by each of the AccountHolder for both Checking and Savings Account.Let the
transactions include the date and time,kindof transaction,Amount,Status
"""

import datetime

class Account:
    def __init__(self,id,accountHolder):
        self.id = id
        self.accountHolder = accountHolder
        self.balance = 0
        self.transactionSummary = []
        print(f"New {type(self)} created: ", self)

    def __repr__(self):
        account_repr = f"Id = {self.id}   Firstname = {self.accountHolder.firstname}  Lastname = {self.accountHolder.lastname}   Address = {self.accountHolder.address}"
        return repr(account_repr)

    def deposit(self,amount):
        self.balance += amount
        transaction = Transaction(datetime.datetime.now(), amount, "Credit", "Success", self.balance)
        self.transactionSummary.append(transaction)
        print(f"{type(self)} Transaction : ", transaction)
        #print(f"{type(self)} Balance : ", self.balance)

    def printTransactions(self):
        #print(f"----All transactions for Account {self.id}----")
        for t in self.transactionSummary:
            print(t)



class AccountHolder:
    def __init__(self, firstname, lastname, address):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address


class CheckingAccount(Account):
    def __init__(self,id,accountHolder):
        super().__init__(id,accountHolder)
        self.withdrawalCounter = 0

    def withdraw(self,amount):
        if self.withdrawalCounter < 6 and amount <= self.balance:
            if amount <= 700:
                self.balance -= amount
                transaction = Transaction(datetime.datetime.now(), amount, "Debit", "Success", self.balance)
                self.transactionSummary.append(transaction)
                print(f"{type(self)} Transaction : ", transaction)
                self.withdrawalCounter += 1
            else:
                print(f"Requested withdrawal of {amount} Amount exceeds $700 for Checking account {self.id}")
                transaction = Transaction(datetime.datetime.now(), amount, "Debit", "Failure", self.balance)
                self.transactionSummary.append(transaction)
                print(f"{type(self)} Transaction : ", transaction)
        else:
            print(f"Requested withdrawal of {amount} Withdrawal limit reached! for Checking account {self.id}")
            transaction = Transaction(datetime.datetime.now(), amount, "Debit", "Failure", self.balance)
            self.transactionSummary.append(transaction)
            print(f"{type(self)} Transaction : ", transaction)

        #print(f"{type(self)} Balance : ", self.balance)


class SavingsAccount(Account):
    def __init__(self, id, accountHolder):
        super().__init__(id, accountHolder)

    def withdraw(self,amount):
        self.balance -= amount
        transaction = Transaction(datetime.datetime.now(), amount, "Debit", "Success", self.balance)
        self.transactionSummary.append(transaction)
        print(f"{type(self)} Transaction : ", transaction)
        #print(f"{type(self)} Balance : ", self.balance)


class Transaction:
    def __init__(self, time, amount, type, status, balance):
        self.time = time
        self.amount = amount
        self.type = type
        self.status = status
        self.balance = balance

    def __repr__(self):
        transaction_repr = f"{self.time}  {self.amount}  {self.type}  {self.status} {self.balance}"
        return repr(transaction_repr)


accountHolder1 = AccountHolder("Raju","Kabre","789, N kirby rd, Collierville, TN, 38097")
checkingaccount1 = CheckingAccount(1111,accountHolder1)
savingsaccount1 = SavingsAccount(1111,accountHolder1)

accountHolder2 = AccountHolder("Balaji","Tupe","132, S Cork rd, Germantown, TN, 34532")
checkingaccount2 = CheckingAccount(2222,accountHolder2)
savingsaccount2 = SavingsAccount(2222,accountHolder2)

accountHolder3 = AccountHolder("Adams","Smith","789, S tipple rd, Nashville, TN, 36722")
checkingaccount3 = CheckingAccount(3333,accountHolder3)
savingsaccount4 = SavingsAccount(3333,accountHolder3)

checkingaccount1.deposit(200)
checkingaccount1.deposit(200)
checkingaccount1.withdraw(435)
checkingaccount1.deposit(200)
savingsaccount1.deposit(2200)
checkingaccount1.withdraw(200)
savingsaccount1.withdraw(100)
savingsaccount1.deposit(2200)
checkingaccount1.deposit(2200)
checkingaccount1.withdraw(100)
checkingaccount1.withdraw(800)
checkingaccount1.deposit(2200)
savingsaccount1.withdraw(200)
savingsaccount1.withdraw(300)
savingsaccount1.withdraw(325)
savingsaccount1.withdraw(125)
savingsaccount1.deposit(200)
savingsaccount1.deposit(2200)
checkingaccount1.deposit(800)
checkingaccount1.withdraw(100)

print(f"----------ALL Checkings Account Transactions for {checkingaccount1.id}------")
checkingaccount1.printTransactions()

print(f"----------ALL Savings Account Transactions for {savingsaccount1.id} ------")
savingsaccount1.printTransactions()

checkingaccount2.deposit(200)
checkingaccount2.deposit(200)
checkingaccount2.deposit(200)
savingsaccount2.deposit(2200)
checkingaccount2.withdraw(200)
checkingaccount2.withdraw(100)
savingsaccount2.deposit(2200)
checkingaccount2.withdraw(4000)
checkingaccount2.deposit(2200)
checkingaccount2.withdraw(100)
checkingaccount2.withdraw(800)
savingsaccount2.withdraw(125)
savingsaccount2.withdraw(200)
savingsaccount2.withdraw(300)
savingsaccount2.withdraw(100)
checkingaccount2.deposit(2200)
savingsaccount2.withdraw(325)
savingsaccount2.deposit(200)
savingsaccount2.deposit(2200)

print(f"----------ALL Checkings Account Transactions for {checkingaccount2.id}------")
checkingaccount2.printTransactions()

print(f"----------ALL Savings Account Transactions for {savingsaccount2.id} ------")
savingsaccount2.printTransactions()


