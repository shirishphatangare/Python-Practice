import tkinter as tk
from tkinter import ttk, filedialog, messagebox

text_contents = dict() # Global dict for checking unsaved changes

# checking unsaved changes
def check_for_changes():
    current = get_text_widget()
    content = current.get("1.0", "end-1c") # Get current contents of text_aread
    name = notebook.tab("current")["text"]

    if hash(content) != text_contents[str(current)]: # If hash of content do not match with stored data in text_contents dict
        if name[-1] != "*":
            notebook.tab("current", text=name + "*") # append * to tab title to indicate unsaved changes
    elif name[-1] == "*":
        notebook.tab("current", text=name[:-1]) # This condition indicates file contents are not changed and hence '*' should be removed from end of tab title


def get_text_widget():
    current_tab = notebook.nametowidget(notebook.select()) # select() method returns the widget name of the currently selected pane
    #print(type(current_tab))   # prints - <class 'tkinter.ttk.Frame'>
    text_widget = current_tab.winfo_children()[0] # current_tab is a frame container and text_widget is text_aread
    #print(type(text_widget))   # prints <class 'tkinter.Text'>

    return text_widget


# close individual tab - Check for unsaved data and user confirmation before closing
def close_current_tab():
    if current_tab_unsaved() and not confirm_close():
        return # do not close current tab

    if len(notebook.tabs()) == 1: # If tab being closed is last tab then create a new default 'untitled' file in a notebook
        create_file()

    current_tab = notebook.nametowidget(notebook.select())
    notebook.forget(current_tab)


# returns (True/False) if current tab is unsaved or not
def current_tab_unsaved():
    text_widget = get_text_widget()
    content = text_widget.get("1.0", "end-1c")
    return hash(content) != text_contents[str(text_widget)]


def confirm_close():
    return messagebox.askyesno(
        message="You have unsaved changes. Are you sure you want to close?",
        icon="question",
        title="Unsaved changes",
    )

# Close all tabs and Exit Application
def confirm_quit():
    unsaved = False

    for tab in notebook.tabs():
        tab_widget = root.nametowidget(tab)
        text_widget = tab_widget.winfo_children()[0]
        content = text_widget.get("1.0", "end-1c")

        if hash(content) != text_contents[str(text_widget)]:
            unsaved = True
            break  # break on first unsaved tab

    if unsaved and not confirm_close():
        return # Do not quit app

    root.destroy() # Pre-emptively terminate an application


def create_file(content="", title="Untitled"):
    container = ttk.Frame(notebook) # 2) Create a Frame and pack it inside a notebook
    container.pack()

    text_area = tk.Text(container)  # 3) Create a text-area inside a frame container
    text_area.insert("end", content)
    text_area.pack(side="left", fill="both", expand=True)

    notebook.add(container, text=title)  # 4) Add a frame container with a text-area to notebook. Notebook contains multiple text-area frames as different tabs
    notebook.select(container)
    # hashing - convert data of arbitrary length to data of specific length. We do not have to store whole file in a dict. hash changes when data changes
    text_contents[str(text_area)] = hash(content)

    text_scroll = ttk.Scrollbar(container, orient="vertical", command=text_area.yview) # Move text-area when scroll bar moves
    text_scroll.pack(side="right", fill="y")
    text_area["yscrollcommand"] = text_scroll.set # Move scroll bar when text-area moves


def open_file():
    file_path = filedialog.askopenfilename()

    try:
        filename = file_path.split("/")[-1]

        with open(file_path, "r") as file:
            content = file.read() # read file contents in content variable

    except (AttributeError, FileNotFoundError):
        print("Open operation cancelled")
        return

    create_file(content, filename)


def save_file():
    file_path = filedialog.asksaveasfilename() # open file dialog

    try:
        filename = file_path.split("/")[-1] # Get file name from file path
        text_widget = get_text_widget() # Get text-area for current tab
        content = text_widget.get("1.0", "end-1c") # Get all the contents of text-area

        with open(file_path, "w") as file:
            file.write(content) # write all file contents to a file

    except (AttributeError, FileNotFoundError):
        print("Save operation cancelled")
        return

    # current is a special tab-id which selects current tab
    notebook.tab("current", text=filename)   # rename current tab to filename
    text_contents[str(text_widget)] = hash(content) # when text contents change, hash inside text_contents dict changes too


def show_about_info():
    messagebox.showinfo(
        title="About",
        message="The Teclado Text Editor is a simple tabbed text editor designed to help you learn Tkinter!",
    )


root = tk.Tk() # Create a root container from Tk object. This root container holds all other components of an editor
root.title("Teclado Text Editor") # Title for main root container (editor) window
# Tkinter options - Control behavior of components in different operating systems
root.option_add("*tearOff", False) # Do not tear off menu or other components from main application window

main = ttk.Frame(root) # Create a frame component in root container
main.pack(fill="both", expand=True, padx=(1), pady=(4, 0)) # Using pack algorithm, define frame position,expansion behavior,padding,fill etc. in root container

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
help_menu = tk.Menu(menubar)

menubar.add_cascade(menu=file_menu, label="File")
menubar.add_cascade(menu=help_menu, label="Help")

file_menu.add_command(label="New", command=create_file, accelerator="Ctrl+N") # command is to define function to call on click of menu button and accelerator is to define ketboard shortcut
file_menu.add_command(label="Open...", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(
    label="Close Tab", command=close_current_tab, accelerator="Ctrl+Q"
)
file_menu.add_command(label="Exit", command=confirm_quit)  # Not on window close button. ONLY on Exit menu button

help_menu.add_command(label="About", command=show_about_info)

notebook = ttk.Notebook(main) # ttk is Themed TK (Improved Tk with more customizations)
notebook.pack(fill="both", expand=True) # 1) Create a Notebook and pack in a main container

create_file()

# Bind keyboard controls to root container so that keyboard shortcuts work without clicking on menu buttons
root.bind("<KeyPress>", lambda event: check_for_changes()) # on key press, check for changes
root.bind("<Control-n>", lambda event: create_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-q>", lambda event: close_current_tab())
root.bind("<Control-s>", lambda event: save_file())

root.mainloop() # Here Tkinter takes control of our application and python program stops here till main editor window is closed
