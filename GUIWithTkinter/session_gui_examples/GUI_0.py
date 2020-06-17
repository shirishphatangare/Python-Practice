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
#Documentation with Example: https://tkdocs.com/tutorial/index.html

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

import tkinter as tk
#The tkinter module, containing the Tk toolkit, has always to be imported.
r = tk.Tk()
#To initialize tkinter, we have to create a Tk root widget, which is a window with a title
# bar and other decoration provided by the window manager. The root widget has to be
# created before any other widgets and there can only be one root widget.
r.title('Counting Seconds')
greeting = tk.Label(text="Hello, Tkinter")
#Label widget. The first parameter of the Label call is the name of the parent window,
# in our case "root". So our Label widget is a child of the root widget.
# The keyword parameter "text" specifies the text to be shown
greeting.pack()
#The pack method tells Tk to fit the size of the window to the given text.
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()
#The window won't appear until we enter the Tkinter event loop

#window.mainloop() tells Python to run the Tkinter event loop. This method listens for events,
# such as button clicks or keypresses, and blocks any code that comes after it from running
# until the window it’s called on is closed.

#Note:tkinter also offers access to the geometric configuration of the widgets which can organize the widgets in the parent windows. There are mainly three geometry manager classes class.
# - pack() method:It organizes the widgets in blocks before placing in the parent widget.
# - grid() method:It organizes the widgets in grid (table-like structure) before placing in the parent widget.
# - place() method:It organizes the widgets by placing them on specific positions directed by the programmer.