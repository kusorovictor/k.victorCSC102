import random
import tkinter as tk
import tkinter.messagebox as messagebox
import banking as bs

class UserView:
    def __init__(self, root):
      self.root = root
      self.root.title("Zenith Banking")
      self.root.geometry("300x200")
      
      username_label = tk.Label(root, text="Username: ")
      username_label.pack(pady=5)
      self.username_entry = tk.Entry(root)
      self.username_entry.pack(pady=5)
      
      submit_button = tk.Button(root, text="Submit", command=self.submit)
      submit_button.pack(pady=5)
      
    def submit(self):
      self.username = self.username_entry.get()
      list =  [bs.CommercialBanking(), bs.GlobalBanking(), bs.RetailBanking()]
      self.division = random.choice(list)
      
      self.root.destroy()  # Close the first window
      
      #Create a new window
      root2 = tk.Tk()
      root2.geometry("300x300")
      message_label = tk.Label(root2, text=f"Welcome {self.username} to Zenith Banking.\nYour banking division is {self.division.get_name()}")
      message_label.pack(pady=5)
      
      #Button to view unique services
      unique_services_button = tk.Button(root2, text="View unique services", command=self.view_unique_services)
      unique_services_button.pack(pady=7)
      
      #Button to view mutual services
      mutual_services_button = tk.Button(root2, text="View mutual services", command=self.view_mutual_services)
      mutual_services_button.pack(padx=5, pady=7)
      root2.mainloop()

    
    def view_unique_services(self):
      messagebox.showinfo("Unique Services", "Your unique services are:\n" + "\n".join(self.division.unique_services()))  
       
    def view_mutual_services(self):
     messagebox.showinfo("Mutual Services", "Your mutual services are:\n" + "\n".join(self.division.mutual_services()))
      
    