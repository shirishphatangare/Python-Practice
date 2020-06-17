#Example: CheckButton: To select any number of options by displaying a number of options to a user as toggle buttons. The general syntax is:
# Syntax: w = CheckButton(master, option=value)

from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
mainloop()