import numpy as np
import pandas as pd


def factorial(a):
    b = int(a)
    for i in range(a-1):
        b *= (i+1)
    print(f'the factorial of {a} is {b}')


def ways_OF_steps(n):
    if n == 2: 
        return 2
    if n ==1:
        return 1
    return ways_OF_steps(n-2) + ways_OF_steps(n-1)


def chance_OF_same_BIRTH(n):
    q = 1 
    for i in range(1, n):
        q *= 1-i/365
    print(f'the chance that at least 2 person  have samebirthday is {1-q}')
    

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


def monte_pi(n):
    random_POSIRION = np.random.uniform(-1, 1, size=[eval(n), 2])
    in_ROUND = 0
    for i, ii in random_POSIRION:
        if i**2+ii**2 <=1:
            in_ROUND += 1
    monte_PI = 4*in_ROUND/eval(n)
    print(f'the pi caclulated by monte-caro used {n} dots is {monte_PI}')
    

def ages_of_children():
    list_OF_oldest = []
    list_OF_sub1 = []
    list_OF_sub2 = []
    for oldest in range(1, 37):
        for sub1 in range(1, oldest):
            for sub2 in range(1, oldest):
                if oldest*sub1*sub2 == 36:
                    list_OF_oldest.append(oldest)
                    list_OF_sub1.append(sub1)
                    list_OF_sub2.append(sub2)
    df_AGE = pd.DataFrame(list(zip(list_OF_oldest,
                                    list_OF_sub1,
                                    list_OF_sub2)), columns=['oldest', 'sub1', 'sub2'])
    df_AGE['ages_sum'] = df_AGE.apply(lambda x: x.sum(), axis=1)
    df_AGE.drop_duplicates(subset='ages_sum', keep=0, inplace=True)
    for age_index in df_AGE.index:
        print(f"if the sum of ages is {df_AGE.loc[age_index, 'ages_sum']},the ages of these children are {df_AGE.loc[age_index, df_AGE.columns[0:-1]].values.tolist()}")


def minest_sum_gap():
    a = np.random.randint(low=0, high=100, size=(5)).tolist()
    b = np.random.randint(low=0, high=100, size=(5)).tolist()
    print(f'a:{a}\nb:{b}')
    list_COMBINED  = a+b
    list_COMBINED.sort(reverse=True)
    a_RESET = []
    b_RESET = []
    for i in range(len(list_COMBINED)):
        if sum(a_RESET) > sum(b_RESET):
            b_RESET.append(list_COMBINED[i])
        else:
            a_RESET.append(list_COMBINED[i])
    print(f'Reseted lists are{a_RESET}{b_RESET}, the minest gap is {abs(sum(a_RESET)-sum(b_RESET))}')
    
    
def hat_COLOR():
    num_OF_red = 3
    num_OF_white = 2
    
    
if __name__ == '__main__':
    # factorial(5)
    print(f'the ways of 100 steps is {ways_OF_steps(30)}')
    # chance_OF_same_BIRTH(100)
    # find_edcba()
    # monte_pi(100)
    # ages_of_children()
    # minest_sum_gap()
    # hat_COLOR()