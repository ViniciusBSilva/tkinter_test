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


##################### button

def enter_clicked():
    l1.configure(text='Enter was clicked')
    
def cancel_clicked():
    l1.configure(text='Cancel was clicked')

bt = tkinter.Button(window, text="Enter", command=enter_clicked)
bt.grid(column=0, row=1)
# bt.pack()

bt2 = tkinter.Button(window, text="Cancel", bg="red", fg="white", command=cancel_clicked)
bt2.grid(column=1, row=1)

# Window Size
window.geometry('350x200')

window.mainloop()