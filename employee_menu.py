import sqlite3

def show_menu():

    print("\n--- Employee Management Systeam ---")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Upadate Employee")
    print("4. Delete Employee")
    print("5. EXIT")

def add_employee():
    
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    emp_id = int(input("Enter employee id: "))
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    salary = int(input("Enter salary: "))

    cursor.execute(
        "INSERT INTO employee (id, name, department, salary) VALUES (?, ?, ?, ?)",
        (emp_id, name, department, salary)
    )

    conn.commit()
    conn.close()

    print("Employee Added Successfully")

def view_employees():

    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()

    if len(employees) == 0:
        print("No employee found")
    else:
        print("\n--- Employee List ---")
        for emp in employees:
            print("ID: ", emp[0], "| Name: ", emp[1], "| Dept: ", emp[2], "| Salary:", emp[3])

    conn.close()

def update_employee():

    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    emp_id = int(input("Enter employee ID to update: "))
    new_salary = int(input("Enter new salary: "))

    cursor.execute(
        "UPDATE employee SET salary = ? WHERE id = ?",
        (new_salary, emp_id)
    )

    if cursor.rowcount == 0:
        print("Employee not found")
    else:
        print("Employee salary updated successfully")

    conn.commit()
    conn.close()

def delete_employee():

    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    emp_id = int(input("Enter employee ID to delete: "))

    cursor.execute(
        "DELETE FROM employee WHERE id = ?",
        (emp_id,)
    )

    if cursor.rowcount == 0:
        print("Employee not found")
    else:
        print("Employee deleted successfully")

    conn.commit()
    conn.close()

while True:
    
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        update_employee()

    elif choice == "4":
        delete_employee()

    elif choice == "5":
        print("Existing Program")
        break

    else:
        print("Invalid Choice")