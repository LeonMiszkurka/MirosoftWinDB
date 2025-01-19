import tkinter as tk

def calculator():
    def btn_click(item):
        current = expression.get()
        expression.set(current + str(item))

    def btn_clear():
        expression.set("")

    def btn_equal():
        try:
            result = str(eval(expression.get()))
            expression.set(result)
        except:
            expression.set("error")

    root = tk.Tk()
    root.title("Calculator")

    expression = tk.StringVar()
    entry = tk.Entry(root, textvariable=expression, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
    entry.grid(row=0, column=0, columnspan=4)

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

    row = 1
    col = 0
    for button in buttons:
        action = lambda x=button: btn_click(x)
        if button == "=":
            action = btn_equal
        elif button == "C":
            action = btn_clear

        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row, column=col)

        col += 1
        if col > 3:
            col = 0
            row += 1

    tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=btn_clear).grid(row=row, column=0)

    root.mainloop()

if __name__ == '__main__':
    calculator()
