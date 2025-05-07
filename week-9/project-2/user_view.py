import tkinter as tk
import employee
from tkinter import messagebox

# Class for the employee interface
class UserView: 
    def __init__(self, root, employees):
        self.employees = employees
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("400x300")

        #Username label and entry
        username_label = tk.Label(self.root, text="Username: ")
        username_label.pack()
        self.username_entry = tk.Entry(self.root)  # Assign to self
        self.username_entry.pack()
        
        #submit button
        submit_button = tk.Button(self.root, text="Submit:", command=self.submit)
        submit_button.pack()
    
    # Submit method to check if the username is in the list of employees
    def submit(self):
        username = self.username_entry.get()  # Access the instance attribute
        
        # Create an Employee instance and check if the username is in the list of employees
        emp = employee.Employee("")
        found_employee = emp.check_employee(username, self.employees)
        
        # If the employee is in the list, take attendance and assign a task to them
        if found_employee is not None:
            found_employee.take_attendance(found_employee, messagebox)
            messagebox.showinfo("Success", "Welcome, " + username + "!")
            found_employee.assign_task(found_employee)
            messagebox.showinfo("Task Assigned", "Your task is: " + found_employee.task.value)
        else:
            emp.refuse_access(messagebox)