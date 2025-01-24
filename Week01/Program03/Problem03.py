# Question 3
# Develop a program that allows us to keep track of two different types of employees.
# - CommissionEmployee represents any employee whose salary consists of a percentage of the total sales made.
# - BaseSalaryPlusCommissionEmployee represents any employee whose salary consists of a base salary plus a percentage of the total sales made
# Use the classes created above to demonstrate their capabilities.

class Employee:

    percentage_of_the_total_sales_made = 8

    def __init__(self, employee_name):
        """Initialize the Employee object."""
        self.employee_name = employee_name

class CommissionEmployee(Employee):

    def __init__(self, employee_name, total_sales_made):
        """Initialize the CommissionEmployee object."""
        super().__init__(employee_name)
        self.total_sales_made = total_sales_made

    def get_salary(self):
        """Get salary of the CommissionEmployee object."""
        return self.total_sales_made * (Employee.percentage_of_the_total_sales_made / 100)

    def get_employee_type(self):
        """Get the employee type."""
        return "Commission Employee"

class BaseSalaryPlusCommissionEmployee(Employee):

    def __init__(self, employee_name, base_salary, total_sales_made):
        """Initialize the BaseSalaryPlusCommissionEmployee object."""
        super().__init__(employee_name)
        self.salary = base_salary
        self.total_sales_made = total_sales_made

    def get_salary(self):
        """Get salary of the BaseSalaryPlusCommissionEmployee object."""
        commission = self.total_sales_made * (Employee.percentage_of_the_total_sales_made / 100)
        return self.salary + commission

    def get_employee_type(self):
        """Get the employee type."""
        return "Base Salary Plus Commission Employee"
