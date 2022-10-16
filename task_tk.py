from tkinter import *

# creating Tk window object
window = Tk()
window.title("Calculator")
window.minsize(width=300, height=300)


# total sum label 
# using the grid function for goementry
total_label = Label(text="Total: ", font=("Arial", 12 , "bold"))
total_label.grid(column=0, row=0)

#  created the calculator output label widget
output = Label(text="0", font=("Arial", 12 , "bold"))
output.grid(column=1, row=0)


# creating calculator entry widget
input = Entry()
input.grid(column=0, row=1)

#  function handling addition
def add_input():
    #  the code below gets the current total and adds the input to it
    current_total = int(output["text"])
    current_total += int(input.get())
    output["text"] = current_total


#  function handling substraction
def substract_input():
    #  the code below gets the current total and substracts the input to it
    current_total = int(output["text"])
    current_total -= int(input.get())
    output.config(text=current_total)

def reset():
        output.config(text=0)

# creating add button widget
add_btn = Button(text="+", command=add_input)
add_btn.grid(column=0, row=2)

# creating substract button widget
substract_btn = Button(text="-", command=substract_input)
substract_btn.grid(column=1, row=2, padx=10)

# creating reset button
reset_btn = Button(text="Reset", command=reset)
reset_btn.grid(column=2, row=2)

# the code below keeps the window open
window.mainloop()