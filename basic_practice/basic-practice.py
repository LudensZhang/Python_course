import numpy as np


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
    print(f'the chance that at least {n} person have samebirthday is {1-q}')

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
    random_POSIRION = np.random.uniform(-1, 1, size=[int(n), 2])
    in_ROUND = 0
    for i, ii in random_POSIRION:
        if i**2+ii**2 <=1:
            in_ROUND += 1
    monte_PI = 4*in_ROUND/int(n)
    print(f'the pi caclulated by monte-caro using {n} dots is {monte_PI}')


if __name__ == '__main__':
    # factorial(5)
    # print(f'the ways of 100 steps is {ways_OF_steps(50)}')
    # chance_OF_same_BIRTH(100)
    # find_edcba()
    # monte_pi(100)