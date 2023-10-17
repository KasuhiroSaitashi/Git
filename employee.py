class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}"

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, salary):
        emp = Employee(name, salary)
        self.employees.append(emp)
        print(f"{name} added to the employee list.")

    def remove_employee(self, name):
        for emp in self.employees:
            if emp.name == name:
                self.employees.remove(emp)
                print(f"{name} removed from the employee list.")
                return
        print(f"Employee {name} not found.")

    def increase_salary(self, name, salary_increase):
        for emp in self.employees:
            if emp.name == name:
                emp.salary += salary_increase
                print(f"{name}'s salary increased by {salary_increase}.")
                return
        print(f"Employee {name} not found.")

    def show_all_employees(self):
        if not self.employees:
            print("No employees to display.")
        else:
            print("List of all employees:")
            for emp in self.employees:
                print(emp)