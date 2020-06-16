class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        #print(SalaryEmployee.__mro__) # MRO of SalaryEmployee is SalaryEmployee --> Employee --> object
        Employee.__init__(self,id, name) # Mention explicitly base class constructor instead of using super() for multiple inheritance conflict resolution
        #super().__init__(id, name) - Using super() here follows Method Resolution Order (MRO) of TemporarySecretary class which is HourlyEmployee constructor
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name) # Using super() is ok here - as per MRO next constructor to be invoked is of Employee class
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission

class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')

class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')

class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')

class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')


#Inheriting from Multiple classes
# In case of multiple inheritance, whenever there is a conflict of base class method/constructor calls MRO of derived class is followed
class TemporarySecretary(Secretary, HourlyEmployee):
    def __init__(self, id, name, weekly_salary):
        Secretary.__init__(self, id, name, weekly_salary)
        print(TemporarySecretary.__mro__) # Prints MRO (Method resolution Order) of TemporarySecretary class to invoke __init__ methods when super() keyword is used


# Try out
# class TemporarySecretary(Secretary, HourlyEmployee):
#     def __init__(self, id, name, weekly_salary, hours_worked, hour_rate):
#         HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)
#         print(TemporarySecretary.__mro__) # Prints MRO (Method resolution Order) of TemporarySecretary class to invoke __init__ methods when super() keyword is used


# Try out
# In case of defining multiple inheritance as below, MRO of TemporarySecretary and default constructors kick in and constructor of Secretary is called by default
# class TemporarySecretary(Secretary, HourlyEmployee):
#     pass