from tkinter import *

root = Tk()
root.title('Simple Calculator')

# Set window size
window_width = 360
window_height = 400

# Get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find the center point
center_x = int((screen_width - window_width) / 2)
center_y = int((screen_height - window_height) / 2)

# Set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)

# Entry
e = Entry(root, width=25, borderwidth=5, font=('Arial', 18))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button dimensions
button_width = 10
button_height = 3

# Functions
def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_addition():
    global f_num, math
    f_num = int(e.get())
    math = 'addition'
    e.delete(0, END)

def button_sub():
    global f_num, math
    f_num = int(e.get())
    math = 'subtraction'
    e.delete(0, END)

def button_mult():
    global f_num, math
    f_num = int(e.get())
    math = 'multiplication'
    e.delete(0, END)

def button_divide():
    global f_num, math
    f_num = int(e.get())
    math = 'division'
    e.delete(0, END)

def button_equal():
    second_number = int(e.get())
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, f_num + second_number)
    elif math == 'subtraction':
        e.insert(0, f_num - second_number)
    elif math == 'multiplication':
        e.insert(0, f_num * second_number)
    elif math == 'division':
        if second_number != 0:
            e.insert(0, f_num / second_number)
        else:
            e.insert(0, "Error")

# Buttons config
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('Clear', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text.isdigit():
        command = lambda x=text: button_add(x)
    elif text == '+':
        command = button_addition
    elif text == '-':
        command = button_sub
    elif text == 'x':
        command = button_mult
    elif text == '/':
        command = button_divide
    elif text == '=':
        command = button_equal
    elif text == 'Clear':
        command = button_clear

    Button(root, text=text, width=button_width, height=button_height, command=command)\
        .grid(row=row, column=col, padx=2, pady=2)

# Footer
label = Label(root, text='This App Developed by Israel Assefa')
label.grid(row=5, column=0, columnspan=4, pady=10)

root.mainloop()

