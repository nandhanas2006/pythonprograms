from tkinter import *
from time import strftime
root = Tk()
root.title("Clock")
def time():
    lbl.config(text=strftime('%H:%M:%S'))
    lbl.after(1000, time)
lbl = Label(root, font=('Arial', 40))
lbl.pack()
time()
root.mainloop()