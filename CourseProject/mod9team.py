# Description: The Module 9 Team Project is a Calulator that execute numbers 1-9 in a calulator item to get the results of the to numbers when you use the operation

# Updated on 3/16/2024

# Updated by: 3/16/2024

# stevaughn borders

# Instructor Nathan Braun

# CSS 225

# Module 9 :Team Project

# This portion of the code saves a window in tkinter to make a folder. The folder is used to process all elements in tkinter that is saved to your desktop and display on the screen.

from tkinter import *

root = Tk()

# This part of the portion code above gives the code a title to refer to when you save it to your device.

root.title("Simple Calculator")

# This portion of the code navigates the display or position of each parameter in tkinter

e = Entry(root, width=35, borderwidth=5)

e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# This portion of the code gives an object a definition of what the object will be executing in the window tkinter has according to what you want to happen when a button is clicked.

def button_click(number):
    current = e.get()

    e.delete(0, END)

    e.insert(0, str(current) + str(number))


# This portion of the code defines an exit command and restart command for the created label button in the tkinter file

def button_clear():
    e.delete(0, END)

    # This portion of the code assigns the tkinter code a list of buttons and the action of each button in the code


def button_operator(operator):
    first_number = e.get()

    global f_num

    global num_operator

    f_num = int(first_number)

    num_operator = operator

    e.delete(0, END)

    # This portion of the code attaches the button number to the addition command to start the calculator


# this is a critical function for the program

# This portion of the code uses the calculator and prints the results from adding two numbers

def button_equal():
    # This portion of the code allows the person to click the second number on the calulator to add to the first number

    second_number = e.get()

    # This portion of the code allows users to revisit the number from the second number if either numbers are not equal or you made a mistake in the calculator

    e.delete(0, END)

    # This portion of the code allows users to add numbers to get a equal results

    if num_operator == '+':

        # This portion of the code computes the numbers you want to add

        e.insert(0, f_num + int(second_number))

    # This portion of the code allows users to multiply numbers to get a equal results

    elif num_operator == '*':

        # This portion of the code computes the numbers you want to multiply to get the results

        e.insert(0, f_num * int(second_number))

        # This portion of the code allows users to divide numbers to get an equal results

    elif num_operator == '/':

        # This portion of the code computes the numbers you want to divide to get the results

        e.insert(0, f_num / int(second_number))

    # This portion of the code allows users to subtract numbers to get a equal results

    elif num_operator == '-':

        # This portion of the code allows you to return the results of the numbers you want to subtract.

        e.insert(0, f_num - int(second_number))

    # This portion of the code allows users to compute a invalid response if the calculation is not able to compute numbers for the type of operator you are using.

    else:

        e.insert(0, "Invalid!!!")

    # NOTE: We did not cover Lambda functions in class. A Lambda Function. However, in Python, when programming on a simulation it is an anonymous function or a function having no name. It is a small and restricted function having no more than one line. In the case below, the Lambda function code is calling the code/function button_click() with the numbers 0-9 as the parameter. Just like a normal function, a Lambda function can have multiple arguments with one expression.


# This portion of the code allows users to choose the numbers 1-9 according to the number and (x,y) coordinates of a grid system. The “Lamba” function allows you to physically press the button to use in the calculator.

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))

button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))

button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))

button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))

button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))

button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))

button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))

button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))

button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

# This portion of the code allows you to position the addition operator button on the calculator

button_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_operator("+"))

# This portion of the code allows you to position the equal operator on the calculator

button_equal = Button(root, text="   =   ", padx=79, pady=20, command=button_equal)

# This portion of the code allows you to position the clear or revise button on the calculator

button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# See the description of a Lambda function above

# This portion of the code allows you to position the subtraction operator button on the calculator

button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: button_operator("-"))

# This portion of the code allows you to position the multiplication operator button on the calculator

# This portion of the code allows you to position the multiply operator button on the calculator

button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: button_operator("*"))

# This portion of the code allows you to position the division operator button on the calculator

button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: button_operator("/"))

# This part of the code is assigning the positions of the numbers 1-9. It is also assigning the positions for the equal, addition, multiplication, division, subtraction and clear button on the display screen of the calculator.

button_1.grid(row=3, column=0)  # This is the position of the number one

button_2.grid(row=3, column=1)  # This is the position of the number two

button_3.grid(row=3, column=2)  # This is the position of the number three

button_4.grid(row=2, column=0)  # This is the position of the number four

button_5.grid(row=2, column=1)  # This is the position of the number five

button_6.grid(row=2, column=2)  # This is the position of the number six

button_7.grid(row=1, column=0)  # This is the position of the number seven

button_8.grid(row=1, column=1)  # This is the position of the number eight

button_9.grid(row=1, column=2)  # This is the position of the number nine

button_0.grid(row=4, column=0)  # This is the position of the number zero

button_add.grid(row=5, column=0)  # This is the position of the number addition(+) button

button_equal.grid(row=5, column=1, columnspan=2)  # This is the position of the equal(=) button

button_clear.grid(row=4, column=1, columnspan=2)  # This is the position of the clear(“CLEAR”) button

button_subtract.grid(row=6, column=0)  # This is the position of the subtraction (-) button

button_multiply.grid(row=6, column=1)  # This is the position of the number multiplication (*) button

button_divide.grid(row=6, column=2)  # This is the position of the division (/) button

# This portion of the code determines the entire programming of the code to tkinter, the device, and the file of your root because it needs an exit function for the calculator to finish the math of the numbers you are using.

root.mainloop()