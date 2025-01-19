import tkinter as tk
from tkinter import Text, filedialog, messagebox
import json
import os

def notepad():
    def save_file():
        text_content = text_area.get("1.0", tk.END)
        current_line = text_area.index(tk.INSERT).split('.')[0]
        file_path = filedialog.asksaveasfilename(defaultextension=".mwText",
                                                 filetypes=[("mwText files", "*.mwText"),
                                                            ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text_content)
            save_metadata(file_path, current_line, text_content)
            save_path_to_file(file_path)
            messagebox.showinfo("Save", "File saved successfully!")

    def save_metadata(file_path, current_line, text_content):
        metadata = {
            "line": current_line,
            "letters": list(text_content)
        }
        json_file_path = file_path.replace('.mwText', '.json')
        with open(json_file_path, 'w') as json_file:
            json.dump(metadata, json_file)

    def save_path_to_file(file_path):
        with open("last_saved_path.txt", 'w') as path_file:
            path_file.write(file_path)

    root = tk.Tk()
    root.title("Notepad")
    root.geometry("600x400")

    menu = tk.Menu(root)
    root.config(menu=menu)
    file_menu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Save", command=save_file)

    text_area = Text(root, wrap='word', font=('Arial', 12))
    text_area.pack(expand='yes', fill='both')

    root.mainloop()

if __name__ == '__main__':
    notepad()
