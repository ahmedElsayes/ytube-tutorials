from tkinter import *

root = Tk()
# root.title("simple entry with button")
e = Entry(root, width=40, borderwidth=5)
e.pack()
e.insert(0, "enter your name: ")
def clicked():
    mytext = e.get()+" is a new programmer"
    mylabel = Label(root, text=mytext)
    mylabel.pack()

# some attributes 'pady', 'padx', 'text', 'command', 'fg'(frontground color), 'bg'(background color)
mybutton = Button(root, text="click me", padx=20, pady=10, fg='red', command=clicked)
mybutton.pack()
root.mainloop()
