import pandas as pd
import numpy as np 
from plotnine import*


def find_edcba():
    for i in range(10000, 30000):
        ls_1 = list(x for x in str(i))
        ls_2 = list(y for y in str(4*i))
        ls_2.reverse()
        if len(ls_2) > 5:
            print("Can't find")
            break
        if ls_1 == ls_2:
            print(f'find the edcba:{i}')
            break
        
        

if __name__ == '__main__':
    find_edcba()
    