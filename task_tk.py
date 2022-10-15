import tkinter

# creating Tk window object
window = tkinter.Tk()
window.title("Calculator")
window.minsize(width=200, height=200)

# total sum label 
# using the grid function for goementry
total = tkinter.Label(text="Total: ", font=("Arial", 12 , "bold"))
total.grid(column=1, row=1)


# the code below keeps the window open
window.mainloop()