#You run a delivery service, and charge people based on their location and weight of their package. The following are some of the things you consider.

#You charge N2000, whenever you are delivering a package with weight of 10kg and above to PAU, and N1500 when it is less.
#However, you charge N5000 whenever you deliver to Epe, a package with weight of 10kg and above, and N4000 when it is less.

#Develop the python GUI program using your knowledge in OOP, that tells a user how much to pay, based on their location, and package weight. 

import tkinter as tk
import user_view

def main():
    root = tk.Tk()
    view = user_view.UserView(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
    