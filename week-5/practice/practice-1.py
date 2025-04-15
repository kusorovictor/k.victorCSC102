import tkinter 
import tkinter.messagebox

#Handling button click event
def button_click():
  print("Button clicked!")
    
  #Show an information message box
  tkinter.messagebox.showinfo("Info: ", "Welcome to COS 102 GUI App!\n")
    
  #Ask for user confirmation
  result = tkinter.messagebox.askyesno("Confirmation", "Do you want to continue?")
  
  
  
#Create the main window 
root = tkinter.Tk() 
root.title("Home Page")
root.geometry("1920x1080")

#Add a label widget 
label = tkinter.Label(root, text = "Hello Friend \n")
label.pack()

#Add a button widget
button = tkinter.Button(root, text = "Click Me!", command=button_click)
button.pack()

#Styling the button widget
button.config(fg = "red", bg = "yellow", font = ("Arial", 12, "bold"), padx = 10, pady = 5)

#Start the event loop
root.mainloop()   
   