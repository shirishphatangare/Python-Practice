#Example:convert the Employee class, which is currently a concrete class, to an abstract
# class. That way, no employee is ever just an Employee, but one that
# implements .calculate_payroll().

#Notes:
#- Abstract base classes exist to be inherited, but never instantiated.
#- Python provides the abc module to define abstract base classes.
#- use leading underscores in your class name to communicate that objects of that class
# should not be created.
#- The abc module in the Python standard library provides functionality
# to prevent creating objects from abstract base classes.
from abc import ABC, abstractmethod

class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')

#Define the Abstract. Base class for any class to be defined as Abstract class is ABC
class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name
    @abstractmethod
    def calculate_payroll(self):
        pass

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
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

#Inheritance can lead you to a huge hierarchical structure of classes that is hard to
# understand and maintain. This is known as the class explosion problem.
# To add new functionality to those classes, use a new file( ProductivitySystem.)