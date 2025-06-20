import tkinter as tk
import user_view

def main():
    root = tk.Tk()
    view = user_view.UserView(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
    