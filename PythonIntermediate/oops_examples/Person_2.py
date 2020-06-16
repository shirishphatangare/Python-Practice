# The attributes are replaced by a contacts dictionary
# The dump method in that class is better implemented as a __str__ special method.
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

    def __str__(self): # This __str__ is never executed due to second __str__ method
        print("Inside first __str__")
        s=''
        for p in sorted(self.contacts):
            s += str(self.contacts[p]) + '\n'
        return s

    def __str__(self):
        print("Inside second __str__")
        s = self.name + '\n'
        if self.mobile is not None:
            s += 'mobile phone:   %s\n' % self.mobile
        if self.office is not None:
            s += 'office phone:   %s\n' % self.office
        if self.private is not None:
            s += 'private phone:  %s\n' % self.private
        if self.email is not None:
            s += 'email address:  %s\n' % self.email
        return(s)


if __name__ == '__main__':
    #Person instances in a dictionary with the name as key
    p1 = Person('Hans Hanson',office_phone='767828283', email='h@hanshanson.com')
    p2 = Person('Ole Olsen', office_phone='767828292')
    p3 = Person('Ali Ahmed', office_phone='767433123')

    phone_book = {'Hanson': p1, 'xAli': p3, 'Olsen': p2}

    print(sorted(phone_book)) # sorted returns list of sorted keys

    print("----------List of Persons----------")
    for person in sorted(phone_book):  # alphabetic order
        print(phone_book[person])
