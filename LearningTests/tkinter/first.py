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
label.pack()

root.mainloop()
