from tkinter import *

def sum():
    variable3.set(float(variable1.get()) + float(variable2.get()))
    clean()
def clean():
    variable1.set("")
    variable2.set("")

root = Tk()
root.config(bd=15)
root.config(cursor="star")

variable1 = StringVar()
variable2 = StringVar()
variable3 = StringVar()

titule1 = Label(root, text="Number 1")
titule1.pack()
entrance1= Entry(root, justify="center", textvariable=variable1)
entrance1.pack()
titule2 = Label(root, text="Number 2")
titule2.pack()
entrance2= Entry(root, justify="center", textvariable=variable2)
entrance2.pack()
titule3 = Label(root, text="Result")
titule3.pack()
entrance3= Entry(root, justify="center", textvariable=variable3)
entrance3.pack()

button= Button(root, text="Sum", command= sum)
button.pack()

root.mainloop()