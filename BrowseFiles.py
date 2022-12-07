from tkinter import *

from tkinter import filedialog

# ('Text Files' '.*txt')  ('CSV files', '*.csv')

# only need to add the function to main project, do not need to add the other stuff
def browseFiles():
    # Add this to main project
    filename = filedialog.askopenfilename(initialdir="/", title='Choose a file', filetypes=[('Text Files', '.*txt')])
    label_file_explorer.configure(text="File Opened: " +filename)
    # Also add this to main project
    file = open(filename, "r")
    # Also add this
    if file:
        data = file.read()
        file.close()
        # Don't need to add this
        label_file_explorer.configure(text="File Text: " + data)

window = Tk()

window.title('File Explorer')


window.config(background = "white")

label_file_explorer = Label(window, text = "File Explorer using Tkinter",
                            width= 100, height = 4,
                            fg = "blue")

button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles)

button_exit = Button(window,
                     text = "Exit",
                     command = exit)

label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)

button_exit.grid(column = 1,row = 3)

# Let the window wait for any events
window.mainloop()