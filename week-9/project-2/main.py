import user_view
import employee
import tkinter as tk


def main():
    employees = [
        employee.Employee("Mary Evans"), employee.Employee("Eyo Ishan"), employee.Employee("Durojaiye Dare"),
        employee.Employee("Adams Ali"), employee.Employee("Andrew Ugwu"), employee.Employee("Stella Mankinde"),
        employee.Employee("Jane Akibo"), employee.Employee("Ago James"), employee.Employee("Michell Taiwo"),
        employee.Employee("Abraham Jones"), employee.Employee("Nicole Anide"), employee.Employee("Kosi Korso"),
        employee.Employee("Adele Martins"), employee.Employee("Emmanuel Ojo"), employee.Employee("Ajayi Fatima")
    ]

    root = tk.Tk()
    root.view = user_view.UserView(root, employees)
    root.mainloop()


if __name__ == "__main__":
    main()
  