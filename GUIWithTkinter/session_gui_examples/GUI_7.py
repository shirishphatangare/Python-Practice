#Example: Listbox: It offers a list to the user from which the user can accept any number of options.
#Syntax is: w = Listbox(master, option=value)
#master is the parameter used to represent the parent window.

from tkinter import *

top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.pack()
top.mainloop()