# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 12:29:31 2022

@author: vinsilva
"""

import tkinter

window = tkinter.Tk()
window.title("GUI")

def click(click, event):
    text = "{} Click!".format(click)
    print(text)
    tkinter.Label(window, text = text)

def left_click(event):
    click("Left", event)
    
def middle_click(event):
    click("Middle", event)
    
def right_click(event):
    click("Right", event)
    
# 'bind' takes 2 parameters 1st is the event name 2nd is the function to bind
# 'Button-1' represents the left click
# 'Button-2' represents the middle click
# 'Button-3' represents the right click
window.bind("Button-1", left_click)
window.bind("Button-2", middle_click)
window.bind("Button-3", right_click)

window.geometry('350x200')
window.mainloop()