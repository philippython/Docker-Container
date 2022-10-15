from tkinter import *

# creating Tk window object
window = Tk()
window.title("Calculator")
window.minsize(width=200, height=200)

# variable storing the sum of calculations
sum_calc = 0

# total sum label 
# using the grid function for goementry
total = Label(text="Total: ", font=("Arial", 12 , "bold"))
total.grid(column=0, row=0)

#  created the calculator output label widget
output = Label(text="0", font=("Arial", 12 , "bold"))
output.grid(column=1, row=0)


# creating calculator entry widget
input = Entry()
input.grid(column=0, row=1)

#  function handling addition
def add_input():
    num = input.get()
    sum_calc += num
    total.config(text=sum_calc)

# creating add button widget
add = Button(text="+", command=add_input)
input.grid(column=0, row=2)

# the code below keeps the window open
window.mainloop()