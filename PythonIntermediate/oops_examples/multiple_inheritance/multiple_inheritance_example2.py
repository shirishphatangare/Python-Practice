#Inheriting from Multiple classes
from oops_examples.Inheritance import hr4, productivity
from oops_examples.multiple_inheritance import employees2

manager = employees2.Manager(1, 'Mary Poppins', 3000)
secretary = employees2.Secretary(2, 'John Smith', 1500)
sales_guy = employees2.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees2.FactoryWorker(4, 'Jane Doe', 40, 15)
temporary_secretary = employees2.TemporarySecretary(5, 'Robin Williams', 400)
company_employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary,  # for TemporarySecretary calculate_payroll() method of SalaryEmployee is always called because in MRO of TemporarySecretary  SalaryEmployee is ahead of HourlyEmployee
]
productivity_system = productivity.ProductivitySystem()
productivity_system.track(company_employees, 40)
payroll_system = hr4.PayrollSystem()
payroll_system.calculate_payroll(company_employees)