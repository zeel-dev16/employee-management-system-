import sqlite3

conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM employee")
employees = cursor.fetchall()

# Insert employee data
emp_id = int(input("Enter employee id: "))
name = input("Enter employee name: ")
department = input("Enter department: ")
salary = int(input("Enter salary: "))

cursor.execute(
    "INSERT INTO employee (id, name, department, salary) VALUES (?, ?, ?, ?)",
    (emp_id, name, department, salary)
    )

if len(employees) == 0:
    print("No employee found")
else:
    print("\nEmployee List :")
    for emp in employees:
        print("ID:", emp[0], "| Name:", emp[1], "| Dept:", emp[2], "| Salary:", emp[3])

conn.commit()
conn.close()

print("Employee added successfully")
