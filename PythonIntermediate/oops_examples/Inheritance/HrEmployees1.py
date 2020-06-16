from oops_examples.Inheritance import hr2

employee = hr2.Employee(1, 'Invalid')
#This should not be done in practice

payroll_system = hr2.PayrollSystem()
# Error would be thrown
payroll_system.calculate_payroll([employee]) # AttributeError: 'Employee' object has no attribute 'calculate_payroll'

#Notes:
#- While you can instantiate an Employee object, the object can’t be used by the
# PayrollSystem as it can’t .calculate_payroll() for an Employee.

