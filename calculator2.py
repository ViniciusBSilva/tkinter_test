# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 13:41:47 2022

@author: vinsilva
"""

from tkinter import *

class CalcButton:
    def __init__(self, frame, text, width, bg, function):
        self.frame = frame
        self.text = text
        self.fg = 'black'
        self.width = width
        self.height = 3
        self.bd = 0
        self.bg = bg
        self.cursor = 'hand2'
        self.command = function

    def create(self):
        return Button(self.frame, 
                      text = self.text,
                      fg = self.fg,
                      width = self.width,
                      height = self.height,
                      bd = self.bd,
                      bg = self.bg,
                      cursor = self.cursor,
                      command = self.command)


class NumCalcButton(CalcButton):
    def __init__(self, frame, text):
        super().__init__(frame, 
                         text, 
                         10, 
                         '#fff', 
                         lambda: btn_click(int(text)))


class ZeroNumCalcButton(CalcButton):
    def __init__(self, frame):
        super().__init__(frame, 
                         '0', 
                         21, 
                         '#fff', 
                         lambda: btn_click(0))


class SpecCalcButton(CalcButton):
    def __init__(self, frame, text):
        super().__init__(frame, 
                         text, 
                         10, 
                         '#eee', 
                         lambda: btn_click(text))


class EqCalcButton(CalcButton):
    def __init__(self, frame, text):
        super().__init__(frame, 
                         text, 
                         10, 
                         '#eee', 
                         lambda: btn_equal())


class ClearCalcButton(CalcButton):
    def __init__(self, frame):
        super().__init__(frame, 
                         'C', 
                         32, 
                         '#eee', 
                         lambda: btn_clear())


class Calculator:
    
    def __init__(self):
        
        self.expression = ''
        
        self.createWindow()
        self.createFrames()
        self.createButtons()
    
    
    def createWindow(self):
        self.window = Tk()
        self.window.geometry('312x324')
        self.window.resizable(0, 0) # this prevents from resizing the window
        self.window.title('Calculator')


    def show(self):
        self.window.mainloop()    
        
        
    def createFrames(self):
        self.input_text = StringVar()
        
        # creating a frame for the input field
        self.input_frame = Frame(self.window, width=312, height=50, 
                            bd=0, highlightbackground='black',
                            highlightcolor='black', highlightthickness=1)
        self.input_frame.pack(side=TOP)
        
        # creating a input field inside the 'Frame'
        input_field = Entry(self.input_frame, font=('arial', 18, 'bold'),
                            textvariable=self.input_text, width=50, bg='#eee',
                            bd=0, justify=RIGHT)
        input_field.grid(row=0, column=0)
        # 'ipady' is internal padding to increase the height of input field
        input_field.pack(ipady=10) 
        
        # creating another 'Frame' for the button below the 'input_frame'
        self.btns_frame = Frame(self.window, width=312, height=272.5, bg='grey')
        self.btns_frame.pack()
        
    
    def createButtons(self):
        # first row
        clear = ClearCalcButton(
            self.btns_frame).create().grid(row=0, column=0, columnspan=3, 
                                           padx=1, pady=1)
        divide = ''
        
        # second row
        seven = ''
        eight = ''
        nine = ''
        multiply = ''
        
        # third row
        four = ''
        five = ''
        six = ''
        minus = ''
        
        # fourth row
        one = ''
        two = ''
        three = ''
        plus = ''
        
        # fifth row
        zero = ''
        point = ''
        equals = ''
        
        
# main
calc = Calculator()    
calc.show()