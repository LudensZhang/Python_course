import pandas as pd
import numpy as np 
from plotnine import*
from tkinter import*

class CalculateBMI:
    def __init__(self):
        window = Tk()
        Label(window, text='name:').grid(row=1, column=3)
        Entry(window).grid(row=1, column=4, padx=5, pady=5)
        label(window, text='height:').grid(row=2, column=3)
        self.height=StringVar()
        Entry(window).grid(textvariable=self.height).grid(row=2, column=4, padx=5, pady=5)
        label(window, text='weight:').grid(row=3, column=3)
        self.weight=StringVar()
        Entry(window, textvariable=self.weight).grid(row=3, column=4, padx=5, pady=5)
        Button(window, text='calculate', command=self.calculate).grid(row=4, column=4, padx=5, pady=5)
        window.mainloop()
        
    def calculate(self):
        result = float(self.weight)/float(self.height)**2
        if result < 18.5:
            print(f'Your BMI is {result}, too slim')
        elif result < 25:
            print()(f'Your BMI is {result}, normal')
        elif result < 30:
            print()(f'Your BMI is {result}, overweight')
        else:
            print(f'Your BMI is {result}, obesity')


    