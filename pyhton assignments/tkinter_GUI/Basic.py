from tkinter import *
root = Tk()

# creat the label widget
Mylabel1 = Label(root, text="welcome future programmer!")
Mylabel2 = Label(root, text="Your first task")

# this is to make the label fixed in the optimum position in the screen
# Mylabel.pack()
# this is to control the position of the item Label, Button, Entry etc
Mylabel1.grid(column=0, row=0)
Mylabel2.grid(column=1, row=1)

# creat a loop lo continously acquire info from the generated msg box
root.mainloop()
