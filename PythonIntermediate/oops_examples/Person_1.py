#Creating class for mobile Phonebook. You are probably familiar with the phone book on your
# mobile phone. The phone book contains a list of persons. For each person you can record
# the name, telephone numbers, email address, and perhaps other relevant data.
# A natural way of representing such personal data in a program is to create a class,
# say class Person. The data attributes of the class hold information like the name, mobile
# phone number, office phone number, private phone number, and email address.
#
# The constructor may initialize some of the data about a person.
# Additional data can be specified later by calling methods in the class.
# One method can print the data.
# Other methods can register additional telephone numbers and an email address.
# In addition we initialize some of the data attributes in a constructor method.

class Person(object):
    def __init__(self, name,
                 mobile_phone=None, office_phone=None,
                 private_phone=None, email=None):
        self.name = name
        self.mobile = mobile_phone
        self.office = office_phone
        self.private = private_phone
        self.email = email

    def add_mobile_phone(self, number):
        self.mobile = number

    def add_office_phone(self, number):
        self.office = number

    def add_private_phone(self, number):
        self.private = number

    def add_email(self, address):
        self.email = address

    def dump(self):
        s = self.name + '\n'
        if self.mobile is not None:
            s += 'mobile phone:   %s\n' % self.mobile
        if self.office is not None:
            s += 'office phone:   %s\n' % self.office
        if self.private is not None:
            s += 'private phone:  %s\n' % self.private
        if self.email is not None:
            s += 'email address:  %s\n' % self.email
        print(s)


p1 = Person('Hans Hanson',office_phone='767828283', email='h@hanshanson.com')
p2 = Person('Ole Olsen', office_phone='767828292')
p2.add_email('olsen@somemail.net')
phone_book = [p1, p2]
# print the phone book
for person in phone_book:
    person.dump()