# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 10:40:35 2022

@author: vinsilva
"""

import tkinter

# Create the window
window = tkinter.Tk()

# Rename window title
window.title("GUI")

# Set label
label = tkinter.Label(window, text = "Hello World!")

# pack is used to show the object in the window
label.pack()

# start main loop - event loop is basically telling the code to keep 
# displaying the window until we manually close it. It runs in an infinite 
# loop in the back-end.
window.mainloop()