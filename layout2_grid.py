# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:20:35 2022

@author: vinsilva
"""

import tkinter
window = tkinter.Tk()
window.title("Test Tkinter Widgets")

f1 = tkinter.Frame(window).grid()

tkinter.Label(f1, text="Username").grid(row=0)
tkinter.Entry(f1).grid(row=0, column=1)

tkinter.Label(f1, text="Password").grid(row=1, column=0)
tkinter.Entry(f1).grid(row=1, column=1)

tkinter.Checkbutton(f1, text = "Keep Me Logged In").grid(columnspan=2)

# Window Size
window.geometry('200x100')
window.mainloop()