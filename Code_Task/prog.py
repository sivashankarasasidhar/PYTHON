#write a python program that allows you to add an employee with domain, name, empid,
#and email details using user input and then print the employee's details.
# Create an empty dictionary to store employee details
#This program defines two functions, add_employee() and print_employee(),
#for adding and printing employee details, respectively.
#It uses a dictionary employee_database to store employee details
#with their Employee IDs as keys. The program runs 
#in a loop, allowing you to add employees, print employee details by Employee ID, or exit the program.
employee_database = {}

# Function to add an employee
def add_employee():
    domain = input("Enter employee domain: ")
    name = input("Enter employee name: ")
    empid = input("Enter employee ID: ")
    email = input("Enter employee email: ")
    
    # Create a dictionary for the employee
    employee = {
        "Domain": domain,
        "Name": name,
        "Employee ID": empid,
        "Email": email
    }
    
    # Add the employee to the database
    employee_database[empid] = employee
    print("Employee added successfully!")

# Function to print employee details
def print_employee(empid):
    employee = employee_database.get(empid)
    if employee:
        print("\nEmployee Details:")
        for key, value in employee.items():
            print(f"{key}: {value}")
    else:
        print("Employee not found.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add Employee")
    print("2. Print Employee Details")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        empid = input("Enter Employee ID to print details: ")
        print_employee(empid)
    elif choice == "3":
        break 
    else:
        print("Invalid choice. Please select 1, 2, or 3.")