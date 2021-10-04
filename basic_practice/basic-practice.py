def factorial(a):
    a = int(a)
    for i in range(a-1):
        a *= (i+1)
    return(a)

def ways_OF_steps():
    ways = 0
    for step_IN_2 in range(51):
        step_IN_1 = (100-step_IN_2*2)
        ways += 
        
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
    ways_OF_steps()
