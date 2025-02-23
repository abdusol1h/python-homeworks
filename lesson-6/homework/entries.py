import os

FILENAME = "employees.txt"

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")
    
    #writing employee information
    with open(FILENAME, "a") as file:
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
    print("Employee record added successfully.")

def view_employees():
    if not os.path.exists(FILENAME):
        print("No records found.")
        return

    with open(FILENAME, "r") as file:
        records = file.readlines()
        if not records:
            print("No records found.")
            return

        for record in records:
            print(record.strip())

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    with open(FILENAME, "r") as file:
        for record in file:
            if record.startswith(emp_id + ","):
                print("Employee Found:", record.strip())
                return
    print("Employee not found.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    records = []
    found = False

    with open(FILENAME, "r") as file:
        records = file.readlines()

    with open(FILENAME, "w") as file:
        for record in records:
            if record.startswith(emp_id + ","):
                found = True
                name = input("Enter new name: ")
                position = input("Enter new position: ")
                salary = input("Enter new salary: ")
                file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                print("Employee record updated.")
            else:
                file.write(record)

    if not found:
        print("Employee not found.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    records = []
    found = False

    with open(FILENAME, "r") as file:
        records = file.readlines()

    with open(FILENAME, "w") as file:
        for record in records:
            if record.startswith(emp_id + ","):
                found = True
                print("Employee record deleted.")
            else:
                file.write(record)

    if not found:
        print("Employee not found.")

def main():
    while True:
        print("\n1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            break
        else:
            print("Invalid input. Please try again.")

main()