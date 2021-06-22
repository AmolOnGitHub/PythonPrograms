# pylint: disable=invalid-name, wrong-import-order, missing-module-docstring, unused-wildcard-import
# pylint: disable=missing-function-docstring, global-statement, multiple-statements, trailing-newlines
# pylint: disable=pointless-statement, trailing-whitespace, redefined-outer-name, wildcard-import

from tkinter import *

root = Tk()
root.title("poggers")

label = Label(
    root, 
    text = "Hello, world"
)
label2 = Label(
    root, 
    text = "Hello again, world"
)
i = 0

label.grid(row = i, column = 0)

root.mainloop()
