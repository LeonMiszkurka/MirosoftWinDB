import tkinter as tk

def settings():
    root = tk.Tk()
    root.title("Settings")
    tk.Label(root, text="Settings Window", font=('Arial', 20)).pack(pady=20)
    root.mainloop()

if __name__ == '__main__':
    settings()
