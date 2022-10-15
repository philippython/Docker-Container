from tkinter import *
import tkinter

# creating Tk window object
window = Tk()
window.title("Calculator")
window.maxsize(width=200, height=200)

# total sum label 
total = tkinter.Label(text="Total", font=("Arial", 12 , "bold"))
total.pack(side="left")


# the code below keeps the window open
window.mainloop()