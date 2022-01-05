# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:20:35 2022

@author: vinsilva
"""

from tkinter import *

window = Tk()

window.title("Test Tkinter Widgets")

label = Label(window, text="Select language: ").pack()

option = StringVar()
option.set(2)


rad1 = Radiobutton(window, text='Python', value=1, var=option).pack()
rad2 = Radiobutton(window, text='Java', value=2, var=option).pack()
rad3 = Radiobutton(window, text='Javascript', value=3, var=option).pack()

# Window Size
window.geometry('350x200')

window.mainloop()