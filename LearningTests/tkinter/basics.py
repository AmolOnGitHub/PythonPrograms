# pylint: disable=invalid-name, wrong-import-order, missing-module-docstring, 
# pylint: disable=missing-function-docstring, global-statement, multiple-statements, 
# pylint: disable=pointless-statement, trailing-whitespace, redefined-outer-name

import tkinter as tk

window = tk.Tk()

# Label - Used to display text on the screen
# Button - Can contain text and performs a function when pressed
# Entry - Allows single-line text input
# Text - Allows multi-line text input
# Frame - A rectangular region used to group widgets or provide padding between widgets

label = tk.Label(
    text = "Python rocks!",
    fg = "#34A2FE",
    bg = "black",
    width = 20, 
    height = 10
)
label.pack()

button = tk.Button(
    text = "Click me!", 
    width = 20,
    height = 5,
    bg = "white",
    fg = "blue"
)
button.pack()

enterT = tk.Label(
    text = "Name",
    fg = "black",   
    width = 20
)
enterT.pack()

entry = tk.Entry(
    fg = "black",
    width = 20
)
entry.pack()

text = entry.get()
entry.delete(0)

window.mainloop()
