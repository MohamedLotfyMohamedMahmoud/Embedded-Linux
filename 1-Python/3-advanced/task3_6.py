import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('employee.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table for employees
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    job TEXT NOT NULL,
    salary REAL NOT NULL
)
''')

# Commit the changes
conn.commit()

def add_employee():
    name = input("Enter employee name: ")
    job = input("Enter employee job: ")
    salary = float(input("Enter employee salary: "))
    
    cursor.execute("INSERT INTO employees (name, job, salary) VALUES (?, ?, ?)", (name, job, salary))
    conn.commit()
    print("Employee added successfully!")

def print_employee():
    emp_id = int(input("Enter employee ID: "))
    
    cursor.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
    employee = cursor.fetchone()
    
    if employee:
        print(f"ID: {employee[0]}")
        print(f"Name: {employee[1]}")
        print(f"Job: {employee[2]}")
        print(f"Salary: {employee[3]}")
    else:
        print("Employee not found.")

def remove_employee():
    emp_id = int(input("Enter employee ID to remove: "))
    
    cursor.execute("DELETE FROM employees WHERE id=?", (emp_id,))
    conn.commit()
    
    if cursor.rowcount:
        print("Employee removed successfully!")
    else:
        print("Employee not found.")

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add new employee")
        print("2. Print employee data")
        print("3. Remove employee from the system")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            print_employee()
        elif choice == '3':
            remove_employee()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Close the connection to the database
conn.close()
