# using property class
class Account:
    def __init__(self, name,balance=0):
        self.first_name=name;
        self.balance = balance

    def setfirstname(self, name):
        print('setname() called')
        self._first_name=name

    def getfirstname(self):
        print('getname() called')
        return self._first_name

    name = property(getfirstname, setfirstname)

    # getter
    def get_balance(self):
        print("Getting value...")
        #The actual balance value is stored in the private _balance variable.
        # The balance attribute is a property object which provides an interface to this
        # private variable.
        return self._balance

    # setter
    def set_balance(self, value):
        print("Setting value...")
        if value < 0:
            raise ValueError("..Balance below 0 is not permitted")
        self._balance = value
    # creating a property object
    balance = property(get_balance, set_balance)
    #The property() method takes the get, set and delete methods as arguments and
    # returns an object of the property class.

account1 = Account("Jess",37)
print(account1.first_name)
print(account1.balance)

account1.name = "Dada"
print(account1.name)

#Trying to set the balance at a negative value
#account1.balance = -300