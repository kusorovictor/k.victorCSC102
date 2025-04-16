
from tkinter import messagebox

def ibeju_lekki(weight):
  if weight < 10:
    messagebox.showinfo("Delivery Cost", "Price of delivery is 3500 naira")
  else:
    messagebox.showinfo("Delivery Cost","Price of delivery is 5000 naira")
    

def epe(weight):
  if weight < 10:
    messagebox.showinfo("Delivery Cost","Price of delivery is 5000 naira")
  else:
    messagebox.showinfo("Delivery Cost","Price of delivery is 10000 naira")
    
