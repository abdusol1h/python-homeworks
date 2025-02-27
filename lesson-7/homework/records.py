import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"

    @staticmethod
    def add_employee(employee):
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(f"{employee.employee_id},{employee.name},{employee.position},{employee.salary}\n")
        print("Employee added successfully!")

    @staticmethod
    def view_all_employees():
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No records found.")
            return
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                print(line.strip())

    @staticmethod
    def search_employee(employee_id):
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(str(employee_id) + ","):
                    print("Employee Found:\n", line.strip())
                    return
        print("Employee not found.")

    @staticmethod
    def update_employee(employee_id, name=None, position=None, salary=None):
        employees = []
        updated = False

        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == str(employee_id):
                    if name:
                        data[1] = name
                    if position:
                        data[2] = position
                    if salary:
                        data[3] = str(salary)
                    updated = True
                employees.append(",".join(data))

        if updated:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                for emp in employees:
                    file.write(emp + "\n")
            print("Employee record updated successfully!")
        else:
            print("Employee not found.")

    @staticmethod
    def delete_employee(employee_id):
        employees = []
        deleted = False

        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if not line.startswith(str(employee_id) + ","):
                    employees.append(line.strip())
                else:
                    deleted = True

        if deleted:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                for emp in employees:
                    file.write(emp + "\n")
            print("Employee record deleted successfully!")
        else:
            print("Employee not found.")

# Example Usage
emp1 = Employee(1001, "John Doe", "Software Engineer", 75000)
EmployeeManager.add_employee(emp1)
EmployeeManager.view_all_employees()
EmployeeManager.search_employee(1001)
EmployeeManager.update_employee(1001, salary=80000)
EmployeeManager.delete_employee(1001)