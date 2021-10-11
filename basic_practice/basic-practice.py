def factorial(a):
    a = int(a)
    for i in range(a-1):
        a *= (i+1)
    return(a)

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
        
        


if __name__ == '__main__':
    # print(factorial(5))
    # print(f'the ways of 100 steps is {ways_OF_steps(50)}')
    # chance_OF_same_BIRTH(100)
    # find_edcba()
    