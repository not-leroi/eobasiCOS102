import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Load the employee data
df = pd.read_csv('GIG-logistics.csv')

# Create the GUI window
root = tk.Tk()
root.title("GIG Logistics Employee Verification")

# Create labels and entry fields
tk.Label(root, text="Enter Employee Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter Department:").grid(row=1, column=0, padx=10, pady=10)
dept_entry = tk.Entry(root)
dept_entry.grid(row=1, column=1, padx=10, pady=10)


# Define the function to verify the employee
def verify_employee():
    name = name_entry.get().strip()
    department = dept_entry.get().strip()

    # Check if employee exists
    employee = df[(df['Name'].str.lower() == name.lower()) & (df['Department'].str.lower() == department.lower())]

    if not employee.empty:
        messagebox.showinfo("Welcome", f"Welcome {name}!")

        # Display other members of the department
        department_members = df[df['Department'].str.lower() == department.lower()]
        members_list = department_members['Name'].tolist()
        members_list.remove(name)  # Remove the employee's own name

        if members_list:
            members_message = "Other members in your department:\n" + "\n".join(members_list)
        else:
            members_message = "You are the only member in this department."

        messagebox.showinfo("Department Members", members_message)
    else:
        messagebox.showwarning("Not Found", f"Sorry, {name} is not an employee in {department} department.")


# Create the Verify button
verify_button = tk.Button(root, text="Verify", command=verify_employee)
verify_button.grid(row=2, column=0, columnspan=2, pady=20)

# Run the GUI
root.mainloop()
