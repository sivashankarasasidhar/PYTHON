'''write a python program that allows you to add an employee with domain, name, empid,
and email details using user input and then print the employee's details.'''
emp_info = {}
def add_employee():
    domain = input("domain: ")
    name = input(" name: ")
    empid = input("ID: ")
    email = input("email: ")
    emply = {
        "Domain": domain,
        "Name": name,
        "Employee ID": empid,
        "Email": email
    }
    emp_info[empid] = emply
    print("Employee added successfully!")
def print_employee_details(empid):
    emply = emp_info.get(empid)
    if emply:
        print("\nEmployee Details:")
        for key, value in emply.items():
            print(f"{key}: {value}")
    else:
        print("Employee not found.")
while True:
    print("\noptions:")
    print("1. add employee")
    print("2. Print employee Details")
    print("3. Exit")
    choice = input("enter your choice (1/2/3): ") 
    if choice == "1":
        add_employee()
    elif choice == "2":
        empid = input("enter Employee ID to print details: ")
        print_employee_details(empid)
    elif choice == "3":
        break 
    else:
        print("Invalid")