# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:20:35 2022

@author: vinsilva
"""

import tkinter

window = tkinter.Tk()
window.title("Test Tkinter Widgets")

##################### combobox
from tkinter.ttk import *
combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(3)
combo.grid(column=0, row=0)

# Window Size
window.geometry('350x200')

window.mainloop()