# ==============================
# IMPORTS
# ==============================

import tkinter as tk
import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from basicop import *
from scientificop import *
from utils import *


# ==============================
# WINDOW SETUP
# ==============================

root = tk.Tk()

root.title("Scientific Calculator")

# Fullscreen Responsive Window
root.state("zoomed")

# Minimum Window Size
root.minsize(900, 600)

# Background Color
root.configure(bg="#1e1e1e")


# ==============================
# DISPLAY FRAME
# ==============================

display_frame = tk.Frame(
    root,
    bg="#1e1e1e"
)

display_frame.pack(
    fill="x",
    padx=20,
    pady=20
)


# ==============================
# DISPLAY
# ==============================

display = tk.Entry(
    display_frame,
    font=("Consolas", 30),
    bd=0,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white",
    justify="right"
)

display.pack(
    fill="x",
    ipadx=8,
    ipady=20
)


# ==============================
# SPECIAL FUNCTIONS
# ==============================

scientific_ops = {

    "sin",
    "cos",
    "tan",

    "cosec",
    "sec",
    "cot",

    "sqrt",
    "cbrt",

    "square",
    "cube",

    "ln",
    "log10",
    "exp",

    "sinh",
    "cosh",
    "tanh",

    "factorial",

    "abs",
    "ceil",
    "floor"
}


# ==============================
# BUTTON FUNCTIONS
# ==============================

def press(value):

    current = display.get()

    display.delete(0, tk.END)

    if value in scientific_ops:

        display.insert(0, current + value + "(")

    else:

        display.insert(0, current + str(value))


def clear():

    display.delete(0, tk.END)


def backspace():

    current = display.get()

    display.delete(0, tk.END)

    display.insert(0, current[:-1])


# ==============================
# CALCULATE
# ==============================

def calculate():

    try:

        expression = display.get()

        expression = expression.replace("^", "**")

        result = eval(
            expression,
            {

                # Trigonometric
                "sin": sin,
                "cos": cos,
                "tan": tan,
                "cosec": cosec,
                "sec": sec,
                "cot": cot,

                # Root
                "sqrt": sqrt,
                "cbrt": cbrt,

                # Power
                "square": square,
                "cube": cube,

                # Log
                "ln": ln,
                "log10": log10,

                # Exponential
                "exp": exp,

                # Hyperbolic
                "sinh": sinh,
                "cosh": cosh,
                "tanh": tanh,

                # Other
                "factorial": factorial,
                "abs": absolute,
                "ceil": ceil,
                "floor": floor,

                # Constants
                "PI": PI,
                "E": E,

                "__builtins__": None
            }
        )

        display.delete(0, tk.END)

        display.insert(0, result)

    except:

        display.delete(0, tk.END)

        display.insert(0, "Error")


# ==============================
# BUTTON FRAME
# ==============================

button_frame = tk.Frame(
    root,
    bg="#1e1e1e"
)

button_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)


# ==============================
# BUTTON LIST
# ==============================

buttons = [

    'sin', 'cos', 'tan', 'cosec', 'sec', 'cot',
    'sqrt', 'cbrt', 'square', 'cube', 'ln', 'log10',

    '7', '8', '9', '/', '%', 'C',
    '4', '5', '6', '*', '^', '←',
    '1', '2', '3', '-', '(', ')',
    '0', '.', 'PI', '+', 'E', '=',

    'sinh', 'cosh', 'tanh', 'exp', 'abs', 'factorial'
]


# ==============================
# RESPONSIVE GRID
# ==============================

total_columns = 6

for i in range(total_columns):

    button_frame.grid_columnconfigure(
        i,
        weight=1
    )

total_rows = (len(buttons) // total_columns) + 1

for i in range(total_rows):

    button_frame.grid_rowconfigure(
        i,
        weight=1
    )


# ==============================
# BUTTON CREATION
# ==============================

row = 0
col = 0

row = 0
col = 0

for button in buttons:

    # ==========================
    # BUTTON COMMANDS
    # ==========================

    if button == '=':

        command = calculate

    elif button == 'C':

        command = clear

    elif button == '←':

        command = backspace

    else:

        command = lambda b=button: press(b)

    # ==========================
    # BUTTON COLORS
    # ==========================

    if button == '=':

        bg_color = "#00a65a"
        active_color = "#008d4c"

    elif button == 'C':

        bg_color = "#d9534f"
        active_color = "#c9302c"

    elif button == '←':

        bg_color = "#f0ad4e"
        active_color = "#ec971f"

    elif button in {
        '+', '-', '*', '/', '%', '^'
    }:

        bg_color = "#3c3f41"
        active_color = "#4b4f52"

    else:

        bg_color = "#2d2d2d"
        active_color = "#404040"

    # ==========================
    # BUTTON CREATION
    # ==========================

    btn = tk.Button(

        button_frame,

        text=button,

        font=("Arial", 16, "bold"),

        bg=bg_color,
        fg="white",

        activebackground=active_color,
        activeforeground="white",

        bd=0,

        command=command
    )

    btn.grid(

        row=row,
        column=col,

        sticky="nsew",

        padx=5,
        pady=5,

        ipadx=10,
        ipady=20
    )

    col += 1

    if col >= total_columns:

        col = 0
        row += 1

# ==============================
# KEYBOARD SUPPORT
# ==============================

def key_press(event):

    key = event.char

    if key in "0123456789+-*/().%^":
        press(key)

    elif key == "\r":
        calculate()

    elif key == "\x08":
        backspace()


root.bind("<Key>", key_press)


# ==============================
# MAIN LOOP
# ==============================

root.mainloop()