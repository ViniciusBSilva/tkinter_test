# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:20:35 2022

@author: vinsilva
"""

import tkinter

window = tkinter.Tk()

window.title("Test Tkinter Widgets")

from tkinter import messagebox

def clicked():
    messagebox.showinfo("Test Title", "Test message")

btn = tkinter.Button(window, text="TEST", command=clicked).pack()

# Window Size
window.geometry('350x200')

window.mainloop()