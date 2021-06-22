# pylint: disable=invalid-name, wrong-import-order, missing-module-docstring, unused-wildcard-import
# pylint: disable=missing-function-docstring, global-statement, multiple-statements, trailing-newlines
# pylint: disable=pointless-statement, trailing-whitespace, redefined-outer-name, wildcard-import

from tkinter import *
from tkmacosx import Button

root = Tk()
root.title("poggers")

def click():
    label = Label(
        root,
        text = "button works pog",
        fg = "blue",
        bg = "black",
    )
    label.grid(row = 1, column = 0)

button = Button(
    root,
    text = "click",
    padx = 20,
    pady = 10,
    command = click,
    fg = "blue",
    bg = "black"
)

button.grid(row = 0, column = 0)

root.mainloop()
