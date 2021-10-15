import pandas as pd
import numpy as np 
from plotnine import*

def Multiplication_table():
    for i in range(1, 10):
        for ii in range(1, i+1):
            print(f'{i}x{ii}={i*ii}', end='')
            for iii in range(3 - len(str(i*ii))):
                print(' ', end='')
        print('\n')


if __name__ == '__main__':
    Multiplication_table()