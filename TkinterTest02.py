# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 12:22:58 2022

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

##################### entry
txt = tkinter.Entry(window, width=10)
txt.grid(column=0, row=2)

def txt_clicked():
    res = "Welcome to " + txt.get()
    l1.configure(text=res)
    
bt_txt = tkinter.Button(window, text="Enter Text", command=txt_clicked)
bt_txt.grid(column=1, row=2)

# Window Size
window.geometry('350x200')

window.mainloop()