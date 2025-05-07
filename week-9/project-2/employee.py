import tasks
import random

class Employee:
    def __init__ (self, name):
      self.name = name
      self.attendance = False
      self.task = "" #Employee's task is empty by default
    
    #Check if an employee is in the list of employees  
    def check_employee(self, username, list):
            for employee in list:
                if username == employee.name:
                    return employee
                    
    
    #Check if an employee has taken attendance, if not, take attendance for them
    def take_attendance(self, employee, messagebox):
        if employee.attendance == False:
            employee.attendance = True
            messagebox.showinfo("Status","Attendance taken.")
            return True
        else:
            messagebox.showinfo("Status","Attendance already taken for this employee.")
            return False
          
    def assign_task(self, employee):
        #Check if the employee already has a task assigned, if not, assign a task to them
        if employee.task == "":
            employee.task = random.choice(list(tasks.Task))
            
    def refuse_access(self, messagebox):
        messagebox.showerror("Error", "Access Denied!")
        return False
        
