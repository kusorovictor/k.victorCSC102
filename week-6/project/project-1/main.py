import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import msgbox


root = tk.Tk()
root.title("Login Form")
root.geometry("500x200")

# Create location label and entry
location_label = tk.Label(root, text="Location:")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

# Create weight label and entry
weight_label = tk.Label(root, text="Weight:")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()


# Create submit button
def submit_callback():
  loc = location_entry.get()
  weight = weight_entry.get()
  if not loc or not weight:
    messagebox.showerror("Error", "Please enter both location and weight")
    location_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    return
  msgbox.submit(location_entry, weight_entry)

submit_button = tk.Button(root, text="Submit", command=submit_callback)
submit_button.pack()

# Run the main event loop
root.mainloop()