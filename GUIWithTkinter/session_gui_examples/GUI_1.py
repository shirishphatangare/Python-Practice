#Python offers multiple options for developing GUI (Graphical User Interface).
#Documentation: https://docs.python-guide.org/scenarios/gui/

# platform-independent GUI toolkits exist for Python are:
# Tkinter
# wxWidgets
# Qt
# Gtk+
# Kivy
# FLTK
# OpenGL
#Note: Some of them haven’t been ported to Python 3 yet. Tkinter and Qt are known to be Python 3-compatible.

# Out of all the GUI methods, tkinter is the most commonly used method.
# It is a standard Python interface to the Tk GUI toolkit shipped with Python.
# Tcl/Tk is fully portable to the Mac OS X, Windows, and Unix platforms.
#Documentation for Tkinter: https://docs.python.org/2/library/tkinter.html

#Flow of A simple GUI with the help of Tkinter


#Steps To create a tkinter app:
#1. Importing the module – tkinter
#2. Create the main window (container) and Initialize it (renaming it is optional)
#3. Add any number of widgets to the main window and decide on the gemetric management
# (to display the widget in size it requires.)
#4. Apply the event Trigger on the widgets(use the mainloop() method to display the window
# until you manually close it. It runs an infinite loop in the backend.)

#Note: name of the module in Python 2.x is ‘Tkinter’ and in Python 3.x it is ‘tkinter’.
import tkinter

#There are two main methods used which the user needs to remember while creating the Python application with GUI.
#1.Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1):
# - To create a main window, tkinter offers a method ‘Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)’.
# - To change the name of the window, you can change the className to the desired one.
#  - The basic code used to create the main window of the application is:
#       m=tkinter.Tk() where m is the name of the main window object
#2. mainloop(): There is a method known by the name mainloop() is used when your application
# is ready to run. mainloop() is an infinite loop used to run the application,
# wait for an event to occur and process the event as long as the window is not closed.

import tkinter

window = tkinter.Tk()
# to rename the title of the window
window.title("GUI")
# pack is used to show the object in the window
label = tkinter.Label(window, text = "Welcome to Tutorial on Tkinter!").pack()
window.mainloop()