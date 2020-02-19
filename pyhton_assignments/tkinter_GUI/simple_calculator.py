from tkinter import *

root = Tk()
root.title('Basic calculator')
# creat an entry. specify width and border width
e = Entry(root, width=30, borderwidth=5)
# the grid is to make the size of all calculator elements consistent with each other
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_press(num):
    # new_num = str(num)
    new_num = e.get() + str(num)
    e.delete(0, END)
    e.insert(0, new_num)

def button_clear():
    e.delete(0, END)

# To create the calculator buttons text, width, length, command
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_press(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_press(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_press(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_press(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_press(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_press(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_press(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_press(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_press(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_press(0))
button_CLEAR = Button(root, text='clear', padx=80, pady=20, command=button_clear)

# now organizing the buttons into grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_CLEAR.grid(row=4, column=1, columnspan=2)


root.mainloop()
