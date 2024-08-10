# Python_intership
import tkinter as tk
def btn_click(item):
    current = display_var.get()
    display_var.set(current + str(item))


def btn_clear():
    display_var.set("")


def btn_equal():
    try:
        result = str(eval(display_var.get()))
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

display_var = tk.StringVar()


display_entry = tk.Entry(root, textvariable=display_var, font=('arial', 18, 'bold'), bd=20, insertwidth=4, width=14, borderwidth=4)
display_entry.grid(row=0, column=0, columnspan=4)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 18, 'bold'), command=btn_equal)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 18, 'bold'), command=lambda t=text: btn_click(t))
    btn.grid(row=row, column=col)

clear_btn = tk.Button(root, text='C', padx=8, pady=8, font=('arial', 18, 'bold'), command=btn_clear)
clear_btn.grid(row=4, column=2, columnspan=2)

root.mainloop()
