from Problem03 import CommissionEmployee, BaseSalaryPlusCommissionEmployee

def main():
    employee1 = CommissionEmployee("Teresa", 50000)
    employee2 = BaseSalaryPlusCommissionEmployee("Mart", 30000, 2480)
    employee3 = CommissionEmployee("Nicolas", 5500)
    employee4 = BaseSalaryPlusCommissionEmployee("Ryan", 2000, 1789)

    employees = [employee1, employee2, employee3, employee4]

    employee_name = input("Enter employee name: ").strip()

    employee_found = None
    for employee in employees:
        if employee.employee_name.lower() == employee_name.lower():
            employee_found = employee
            break

    if employee_found:
        print(f"Name: {employee_found.employee_name}")
        print(f"Employee Type: {employee_found.get_employee_type()}")
        print(f"Salary: {employee_found.get_salary()}")
    else:
        print("Employee not found.")

main()