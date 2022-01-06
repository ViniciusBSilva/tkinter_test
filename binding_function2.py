# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 12:29:31 2022

@author: vinsilva
"""

import tkinter

window = tkinter.Tk()
window.title("GUI")

def say_hi(event):
    print("hi")
    tkinter.Label(window, text="Hi").pack()
    
btn = tkinter.Button(window, text = "Click Me!")

# 'bind' takes 2 parameters 1st is the event name 2nd is the function to bind
# 'Button-1' represents the left click
# 'Button-2' represents the middle click
# 'Button-3' represents the right click
btn.bind("Button-1", say_hi)
btn.pack()

window.geometry('350x200')
window.mainloop()