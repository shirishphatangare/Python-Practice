import tkinter as tk
from tkinter import ttk


def greet():
    # The get() method is used to fetch the value of a StringVar() instance.
    # If user_name is empty, print Hello, World!
    print(f"Hello, {user_name.get() or 'World'}!")


root = tk.Tk()
root.title("Greeter")

# Here we create an instances of the StringVar() class, which is to track the content of widgets
user_name = tk.StringVar()

name_label = ttk.Label(root, text="Name: ")  # Label
name_label.pack(side="left", padx=(0, 10))   # pack Label
name_entry = ttk.Entry(root, width=15, textvariable=user_name) # Textbox
name_entry.pack(side="left") # pack Textbox
name_entry.focus()

greet_button = ttk.Button(root, text="Greet", command=greet) # button
greet_button.pack(side="left", fill="x", expand=True)  # pack button - Notice when you expand main window, only greet button is expanded on horizontal axis

root.mainloop()