import pandas as pd
import numpy as np 
from plotnine import*


class BMI():
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    
    def calculate(self):
        result = self.weight/self.height**2
        if result < 18.5:
            print(f'Your BMI is {result}, too slim')
        elif result < 25:
            print(f'Your BMI is {result}, normal')
        elif result < 30:
            print(f'Your BMI is {result}, overweight')
        else:
            print(f'Your BMI is {result}, obesity')


if __name__ == '__main__':
    a = BMI(1.7, 60)
    a.calculate()