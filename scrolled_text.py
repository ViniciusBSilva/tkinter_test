# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:20:35 2022

@author: vinsilva
"""

import tkinter

window = tkinter.Tk()

window.title("Test Tkinter Widgets")

from tkinter import scrolledtext
txt = scrolledtext.ScrolledText(window, width=40, height=10)

txt.insert("insert", "111111111111111111111111111111111111111111111111111")

txt.insert("insert", "222222222222222222222222222222222222222222222222222")

txt.insert("end", "3333333333333333333333333333333333333333333333333333")

txt.pack()

# Window Size
window.geometry('350x200')

window.mainloop()