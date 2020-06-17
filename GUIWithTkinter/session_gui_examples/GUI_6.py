#Example: Label: It refers to the display box where you can put any text or image which can be updated any time as per the code.
#Syntax is: w=Label(master, option=value)
#master is the parameter used to represent the parent window.

from tkinter import *
root = Tk()
w = Label(root, text='TextforLabel')
w.pack()
root.mainloop()