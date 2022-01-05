# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:20:35 2022

@author: vinsilva
"""

import tkinter

window = tkinter.Tk()

window.title("Test Tkinter Widgets")

##################### label
l1 = tkinter.Label(window, text="Vinicius!", font=("Arial", 12))
l1.grid(column=0, row=0)
# l1.pack()


# Window Size
window.geometry('350x200')

window.mainloop()