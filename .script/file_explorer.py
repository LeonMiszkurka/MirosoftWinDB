import os
import tkinter as tk
from tkinter import filedialog

def file_explorer():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename()
    if file_path:
        os.system(f'explorer /select,"{file_path}"')

if __name__ == '__main__':
    file_explorer()
