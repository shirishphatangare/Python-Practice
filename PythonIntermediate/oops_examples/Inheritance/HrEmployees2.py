from oops_examples.Inheritance import hr3, employees, productivity

employee = hr3.Employee(1, 'Invalid') # TypeError: Can't instantiate abstract class Employee with abstract methods calculate_payroll
payroll_system = hr3.PayrollSystem()
# Error would be thrown
payroll_system.calculate_payroll([employee])

#Notes:
#- the class cannot be instantiated because it contains an abstract method
# calculate_payroll()

