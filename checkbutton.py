# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:20:35 2022

@author: vinsilva
"""

import tkinter

window = tkinter.Tk()

window.title("Test Tkinter Widgets")


chk_state = tkinter.BooleanVar()
chk_state.set(True)

def toogle():
    text = str(chk_state.get())
    label = tkinter.Label(window, text="Checkbox is = {}".format(text))
    label.grid(column=0, row=1)  


chk = tkinter.Checkbutton(window, text="Select", var=chk_state, command=toogle)
chk.grid(column=0, row=0)


# Window Size
window.geometry('350x200')

window.mainloop()