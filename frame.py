# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 13:20:35 2022

@author: vinsilva
"""

import tkinter
window = tkinter.Tk()
window.title("Test Tkinter Widgets")

# creating frames to separete the window
top_frame = tkinter.Frame(window).pack()
botton_frame = tkinter.Frame(window).pack()

# adding buttons to top frame
btn1 = tkinter.Button(top_frame, text="Button 1").pack()
btn2 = tkinter.Button(top_frame, text="Button 2").pack()

# adding buttons to botton frame
btn3 = tkinter.Button(botton_frame, text="Button 3").pack(side="left")
btn4 = tkinter.Button(botton_frame, text="Button 4").pack(side="left")
btn5 = tkinter.Button(botton_frame, text="Button 5").pack(side="right")

# Window Size
window.geometry('350x200')
window.mainloop()