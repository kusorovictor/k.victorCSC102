import tkinter as tk
import service
from tkinter import messagebox

# Class for the delivery service interface
class UserView: 
  
  def __init__(self, root):
    self.root = root
    self.root.title("Delivery Service")
    self.root.geometry("400x300")
    
    # Labels and entries for location and weight
    location_label = tk.Label(self.root, text="Location:")
    location_label.pack()
    self.location_entry = tk.Entry(self.root)
    self.location_entry.pack()
    
    weight_label = tk.Label(self.root, text="Weight (kg):")
    weight_label.pack()
    self.weight_entry = tk.Entry(self.root)
    self.weight_entry.pack()

    
    
    # Submit button to calculate cost
    submit_button = tk.Button(self.root, text="Submit:", command=self.submit)
    submit_button.pack()
    
    
  
    # Submit method to calculate cost based on location and weight
  def submit(self):
    location = self.location_entry.get().lower() #for consistency
    weight = float(self.weight_entry.get())
      
      # Create a service instance and calculate cost
    my_service = service.delivery_service(location, weight)
    if location == "pau":
      my_service.pau_calculate_cost()
    elif location == "epe":
      my_service.epe_calculate_cost()
    else:
      messagebox.showerror("Error", "We do not deliver to this location yet.")
      return
      
    # Display the cost to the user
    messagebox.showinfo("Cost", f"The cost for delivery to {location} is N{my_service.cost}.")
  