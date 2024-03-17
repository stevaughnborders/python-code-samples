


from tkinter import *
root = Tk()  # Creates the main window for the calculator
root.title("Simple Calculator")  # Sets the title of the window

e = Entry(root, width=35, borderwidth=5)  # Creates an input field for the calculator
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)  # Places the input field in the window

# Defines a function to add a number to the input field when a number button is clicked
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Defines a function to clear the input field when the clear button is clicked
def button_clear():
    e.delete(0, END)

# Defines a function to handle arithmetic operations (+, -, *, /) when an operator button is clicked
def button_operator(operator):
    global first_num
    global num_operator
    first_num = e.get()
    num_operator = operator
    e.delete(0, END)

# Defines a function to calculate the result when the equal button is clicked
def button_equal():
    second_num = e.get()
    e.delete(0, END)
    if num_operator == '+':
        e.insert(0, int(first_num) + int(second_num))
    elif num_operator == '-':
        e.insert(0, int(first_num) - int(second_num))
    elif num_operator == '*':
        e.insert(0, int(first_num) * int(second_num))
    elif num_operator == '/':
        e.insert(0, int(first_num) / int(second_num))
    else:
        e.insert(0, "Invalid!!!")

# Creates number buttons (0-9) and assigns them to the button_click function using lambda functions
# Similar buttons created for operator buttons (+, -, *, /), clear button, and equal button

# Grids the buttons in the window
# Each button is placed in a specific row and column in the window using the grid method

root.mainloop()  # Starts the main event loop to display the calculator window and handle user interactions