# The attributes are replaced by a contacts dictionary
# The dump method in that class is better implemented as a __str__ special method.
from oops_examples.Person_2 import Person

class PhoneBook(object):
    def __init__(self):
        self.contacts = {}   # dict of Person instances

    def add(self, name, mobile=None, office=None, private=None, email=None):
        p = Person(name, mobile, office, private, email)
        self.contacts[name] = p

    #Printing the object. A __str__ can print the phone book in alphabetic order:
    def __str__(self):
        s=''
        for p in sorted(self.contacts):
            s += str(self.contacts[p]) + '\n'
        return s

    #To retrieve a Person instance, we use the __call__ with the person's name as argument:
    def __call__(self, name):
        return self.contacts[name]

    def tailoredsort_display(self):
        s = ''
        for n,p in sorted(self.contacts.items(), key = lambda x : x[1].name.split()[-1]):
            s += str(self.contacts[n]) + '\n'
        return s


#Demonstrate Phone Book
b = PhoneBook()
b.add('Ole zen', office='767828292',email='olsen@somemail.net')
b.add('Hans ken',office='767828283', mobile='995320221')
b.add('Per person', mobile='906849781')
#print('Per Person',b('Per Person'))
#print(b)
print(b.tailoredsort_display()) # Sorting on the last name of Person object