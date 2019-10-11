#!/usr/bin/env python3

"""
Write a GUI program to create a simple calculator
layout that looks like the screenshot.

Try to be as Pythonic as possible - it's ok if you
end up writing repeated Button and Grid statements,
but consider using lists and a for loop.

There is no need to store the buttons in variables.

As an optional extra, refer to the documentation to
work out how to use minsize() to prevent your window
from being shrunk so that the widgets vanish from view.

Hint: You may want to use the widgets .winfo_height() and
winfo_width() methods, in which case you should know that
they will not return the correct results unless the window
has been forced to draw the widgets by calling its .update()
method first.

If you are using Windows you will probably find that the
width is already constrained and can't be resized too small.
The height will still need to be constrained, though.
"""

import tkinter

mainWindow = tkinter.Tk()

# title
mainWindow.title('Calculator')
mainWindow.geometry('248x252')
mainWindow['padx'] = 8

# text box
resultBox = tkinter.Entry(mainWindow)
resultBox.grid(row=0, column=0, sticky='nsew')

# button alignment
calcButtons = [[('C', 1), ('CE', 1)],
               [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
               [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
               [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
               [('0', 1), ('=', 2), ('/', 1)]
               ]

calcPad = tkinter.Frame(mainWindow)
calcPad.grid(row=1, column=0, sticky='news')

row = 0
for keyRow in calcButtons:
    col = 0
    for keyColumn in keyRow:
        tkinter.Button(calcPad, text=keyColumn[0]).grid(row=row, column=col, columnspan=keyColumn[1], sticky=tkinter.E + tkinter.W)
        col += keyColumn[1]
    row += 1
mainWindow.update()

# window sizes
mainWindow.minsize(calcPad.winfo_width() + 8, resultBox.winfo_height() + calcPad.winfo_height())
mainWindow.maxsize(calcPad.winfo_width() + 8 + 50, resultBox.winfo_height() + calcPad.winfo_height() + 50)

mainWindow.mainloop()
