import user_view as uv
import tkinter as tk

def main():
    root = tk.Tk()
    userview = uv.UserView(root)
    root.mainloop()

if __name__ == "__main__":
    main()