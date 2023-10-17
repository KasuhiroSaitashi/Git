from employee import Employee, EmployeeManager

def main():
    employee_manager = EmployeeManager()

    while True:
        print("Employee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Increase Salary")
        print("4. Show All Employees")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter employee name: ")
            salary = float(input("Enter employee salary: "))
            employee_manager.add_employee(name, salary)
        elif choice == '2':
            name = input("Enter the name of the employee to remove: ")
            employee_manager.remove_employee(name)
        elif choice == '3':
            name = input("Enter the name of the employee: ")
            salary_increase = float(input("Enter the salary increase: "))
            employee_manager.increase_salary(name, salary_increase)
        elif choice == '4':
            employee_manager.show_all_employees()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()