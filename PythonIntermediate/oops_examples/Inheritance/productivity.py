#Example: tracks productivity based on employee roles
#Managers: Salaried employees.
#Secretaries: Salaried employees .
#Sales employees: have a salary, but they also get commissions for sales.
#Factory workers: paid by the hour.


class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print('')