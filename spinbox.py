# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:20:35 2022

@author: vinsilva
"""

import tkinter

window = tkinter.Tk()

window.title("Test Tkinter Widgets")

spin = tkinter.Spinbox(window, from_=0, to=100, width=5)
spin.pack()

# Window Size
window.geometry('350x200')

window.mainloop()