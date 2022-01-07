# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 13:41:47 2022

@author: vinsilva
"""

import tkinter as tk

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
        return tk.Button(self.frame, 
                      text = self.text,
                      fg = self.fg,
                      width = self.width,
                      height = self.height,
                      bd = self.bd,
                      bg = self.bg,
                      cursor = self.cursor,
                      command = self.command)


class NumCalcButton(CalcButton):
    def __init__(self, frame, text, function):
        super().__init__(frame, 
                         text, 
                         10, 
                         '#eee', 
                         function)


class ZeroNumCalcButton(CalcButton):
    def __init__(self, frame, function):
        super().__init__(frame, 
                         '0', 
                         21, 
                         '#eee', 
                         function)


class SpecCalcButton(CalcButton):
    def __init__(self, frame, text, function):
        super().__init__(frame, 
                         text, 
                         10, 
                         '#ccc', 
                         function)


class EqCalcButton(CalcButton):
    def __init__(self, frame, function):
        super().__init__(frame, 
                         '=', 
                         10, 
                         '#666', 
                         function)


class ClearCalcButton(CalcButton):
    def __init__(self, frame, function):
        super().__init__(frame, 
                         'C', 
                         32, 
                         '#ccc', 
                         function)


class Calculator:
    
    def __init__(self):
        
        self.expression = ''
        
        self.createWindow()
        self.createFrames()
        self.createButtons()
    
    
    def createWindow(self):
        self.window = tk.Tk()
        self.window.geometry('312x324')
        self.window.resizable(0, 0) # this prevents from resizing the window
        self.window.title('Calculator')


    def show(self):
        self.window.mainloop()    
        
        
    def createFrames(self):
        self.input_text = tk.StringVar()
        
        # creating a frame for the input field
        self.input_frame = tk.Frame(self.window, width=312, height=50, 
                            bd=0, highlightbackground='black',
                            highlightcolor='black', highlightthickness=1)
        self.input_frame.pack(side=tk.TOP)
        
        # creating a input field inside the 'Frame'
        self.input_field = tk.Entry(
            self.input_frame, font=('arial', 18, 'bold'),
            textvariable=self.input_text, width=50, bg='#333', fg='white',
            bd=0, justify=tk.RIGHT)
        self.input_field.grid(row=0, column=0)
        # 'ipady' is internal padding to increase the height of input field
        self.input_field.pack(ipady=10) 
        
        # creating another 'Frame' for the button below the 'input_frame'
        self.btns_frame = tk.Frame(
            self.window, width=312, height=272.5, bg='grey')
        self.btns_frame.pack()
        
    
    def createButtons(self):
        # first row
        btn_clear = self.createClearCalcButton().grid(
            row=0, column=0, columnspan=3, padx=1, pady=1)
        btn_divide = self.createSpecCalcButton('/').grid(
            row=0, column=3,  padx=1, pady=1)
        
        # second row
        btn_seven = self.createNumCalcButton('7').grid(
            row=1,column=0, padx=1, pady=1)
        btn_eight = self.createNumCalcButton('8').grid(
            row=1,column=1, padx=1, pady=1)
        btn_nine = self.createNumCalcButton('9').grid(
            row=1,column=2, padx=1, pady=1)
        btn_multiply = self.createSpecCalcButton('*').grid(
            row=1, column=3, padx=1, pady=1)
        
        # third row
        btn_four = self.createNumCalcButton('4').grid(
            row=2,column=0, padx=1, pady=1)
        btn_five = self.createNumCalcButton('5').grid(
            row=2,column=1, padx=1, pady=1)
        btn_six = self.createNumCalcButton('6').grid(
            row=2,column=2, padx=1, pady=1)
        btn_minus = self.createSpecCalcButton('-').grid(
            row=2, column=3, padx=1, pady=1)
        
        # fourth row
        btn_one = self.createNumCalcButton('1').grid(
            row=3,column=0, padx=1, pady=1)
        btn_two = self.createNumCalcButton('2').grid(
            row=3,column=1, padx=1, pady=1)
        btn_three = self.createNumCalcButton('3').grid(
            row=3,column=2, padx=1, pady=1)
        btn_plus = self.createSpecCalcButton('+').grid(
            row=3, column=3, padx=1, pady=1)
        
        # fifth row
        btn_zero = self.createZeroNumCalcButton().grid(
            row=4, column=0, columnspan=2, padx=1, pady=1)
        btn_point = self.createSpecCalcButton('.').grid(
            row=4, column=2, padx=1, pady=1)
        btn_equals = self.createEqCalcButton().grid(
            row=4, column=3, padx=1, pady=1)
                                          
    def createNumCalcButton(self, text):
        return NumCalcButton(
            self.btns_frame, 
            text, 
            lambda: self.btnClick(text)).create()

    def createZeroNumCalcButton(self):
        return ZeroNumCalcButton(
            self.btns_frame, 
            lambda: self.btnClick('0')).create()

    def createSpecCalcButton(self, text):
        return SpecCalcButton(
            self.btns_frame, 
            text, 
            lambda: self.btnClick(text)).create()
        
    def createEqCalcButton(self):
        return EqCalcButton(
            self.btns_frame, 
            lambda: self.btnEqual()).create()
    
    def createClearCalcButton(self):
        return ClearCalcButton(
            self.btns_frame, 
            lambda: self.btnClear()).create()
                                            
    def btnClick(self, item):
        self.expression = self.expression + item
        self.input_text.set(self.expression)
    
    def btnClear(self):
        self.expression = ''
        self.input_text.set('')
    
    def btnEqual(self):
        # 'eval' function evalutes the string expression directly
        result = str(eval(self.expression))
        self.input_text.set(result)
        self.expression = ''
        
# main
calc = Calculator()    
calc.show()