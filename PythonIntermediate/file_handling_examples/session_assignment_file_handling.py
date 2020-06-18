"""
1. Read the Account details from a csv/json file
2. Writing the details in individual files
Account Information: Account.csv/Account.json
Transaction : Transcation.csv/Transaction.json
"""

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
import csv
import json

class Account:
    def __init__(self,accountHolder):
        self.id = accountHolder.id
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

    def writeTransactions_csv(self):
        with open("resources/transactions.csv","a") as csv_writer:
            writer = csv.writer(csv_writer,delimiter='\n')
            writer.writerow(self.transactionSummary)

    def updateTransactions_json(self):
        for transaction in self.transactionSummary:
            transaction_list.append(dict(time=f"{transaction.time}",amount=transaction.amount,type=transaction.type,status=transaction.status,balance=transaction.balance))


class AccountHolder:
    def __init__(self, id, firstname, lastname, address):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.address = address


class CheckingAccount(Account):
    def __init__(self,accountHolder):
        super().__init__(accountHolder)
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
    def __init__(self, accountHolder):
        super().__init__(accountHolder)

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
        transaction_repr = f"{self.time},{self.amount},{self.type},{self.status},{self.balance}"
        return transaction_repr

transaction_list = [] # Global list of dicts for json dump


def read_account_details_csv():
    account_details = []
    with open("resources/account.csv", "rt") as csv_file:
        account_data = csv.reader(csv_file)
        for row in account_data:
            account_details.append(AccountHolder(*row))
        return account_details

def read_account_details_json():
    account_details = []
    with open("resources/account.json", "rt") as json_file:
        account_data = json.load(json_file)
        for row in account_data:
            account_details.append(AccountHolder(**row))
        return account_details

def writeTransactions_json():
        with open("resources/transactions.json","w") as json_writer:
            json.dump(transaction_list,json_writer)


#for account_detail in read_account_details_csv():
for account_detail in read_account_details_json():
    checkingaccount = CheckingAccount(account_detail)
    savingsaccount = SavingsAccount(account_detail)

    checkingaccount.deposit(200)
    checkingaccount.deposit(200)
    checkingaccount.withdraw(435)
    checkingaccount.deposit(200)
    savingsaccount.deposit(2200)
    checkingaccount.withdraw(200)
    savingsaccount.withdraw(100)
    savingsaccount.deposit(2200)
    checkingaccount.deposit(2200)
    checkingaccount.withdraw(100)
    checkingaccount.withdraw(800)
    checkingaccount.deposit(2200)
    savingsaccount.withdraw(200)
    savingsaccount.withdraw(300)
    savingsaccount.withdraw(325)
    savingsaccount.withdraw(125)
    savingsaccount.deposit(200)
    savingsaccount.deposit(2200)
    checkingaccount.deposit(800)
    checkingaccount.withdraw(100)

    print(f"----------ALL Checkings Account Transactions for {checkingaccount.id}------")
    #checkingaccount.writeTransactions_csv()
    checkingaccount.updateTransactions_json() # update global list of dicts

    print(f"----------ALL Savings Account Transactions for {savingsaccount.id} ------")
    #savingsaccount.writeTransactions_csv()
    savingsaccount.updateTransactions_json() # update global list of dicts
    print("-" * 50)

writeTransactions_json() # Write global list of dicts to a output json file

