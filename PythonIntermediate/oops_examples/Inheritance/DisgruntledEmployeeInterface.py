#In Python, you don’t have to explicitly declare an interface. Any object that implements
# the desired interface can be used in place of another object. This is known as duck typing

class DisgruntledEmployee:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    #class doesn’t derive from Employee, but it exposes the same interface
    # required by the PayrollSystem.
    def calculate_payroll(self):
        return 1000000

from oops_examples.Inheritance import hr2, employees, productivity

salary_employee = hr2.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = hr2.HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = hr2.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
disgruntled_employee = DisgruntledEmployee(20000, 'Anonymous')
payroll_system = hr2.PayrollSystem()

payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee,
    disgruntled_employee
])

#Note: you don’t have to derive from a specific class for your objects to be reusable by the program
#When to use inheritance instead of just implementing the desired interface
#1. Use inheritance to reuse an implementation: Your derived classes should leverage most
# of their base class implementation. They must also model an is a relationship.
# A Customer class might also have an id and a name, but a Customer is not an Employee,
# so you should not use inheritance.
#2. Implement an interface to be reused: When you want your class to be reused by a
# specific part of your application, you implement the required interface in your class,
# but you don’t need to provide a base class, or inherit from another class.