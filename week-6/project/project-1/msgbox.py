
from tkinter import messagebox
import check_values

def submit(location_entry, weight_entry):
    #Get the location from the entry box
    location = location_entry.get()
    
    #Get the weight from the entry box
    weight = int(weight_entry.get())
    
    #Check if the location and weight are not empty
    check_location_weight(location, weight)
    

def check_location_weight(location, weight):
    #Check if the location and weight are not empty
    if location and weight:
        if location.lower() == "ibeju lekki":
            check_values.ibeju_lekki(weight)
        elif location.lower() == "epe":
            check_values.epe(weight)
        else: 
            #Display an error message box
            messagebox.showerror("Error", "Location not recognized. Please enter a valid location.")
            
