# 基础编程作业
0. 导入需要的包 
```
import numpy as np
import pandas as pd
```
1. 100 的阶乘是多少?(华为工程师面试题目)
```
def factorial(a):
    b = int(a)
    for i in range(a-1):
        b *= (i+1)
    print(f'the factorial of {a} is {b}')
```
2. 一只青蛙一次只能跳一级或者两级台阶，青蛙跳到 100 级台阶有多少中跳法?(google 工程师面试题目)
```
def ways_OF_steps(n):
    if n == 2: 
        return 2
    if n ==1:
        return 1
    return ways_OF_steps(n-2) + ways_OF_steps(n-1)
```
3. 100 个人集中在一个房间，至少有两个人生日相同的概率有多大?(微软工程师面试题目) 
```
def chance_OF_same_BIRTH(n):
    q = 1 
    for i in range(1, n):
        q *= 1-i/365
    print(f'the chance that at least 2 person  have samebirthday is {1-q}')
```
4. 有一个五位数 abcde，乘以 4 以后变成 edcba，abcde 是多少?Apple 实习面试题目)
```
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
```
5. 运用 Monte Carno 方法计算圆周率的近似值。
```
def monte_pi(n):
    random_POSIRION = np.random.uniform(-1, 1, size=[eval(n), 2])
    in_ROUND = 0
    for i, ii in random_POSIRION:
        if i**2+ii**2 <=1:
            in_ROUND += 1
    monte_PI = 4*in_ROUND/eval(n)
    print(f'the pi caclulated by monte-caro used {n} dots is {monte_PI}')
```
6. 一普查员问一位女士,“你有多少个孩子,他们多少岁?”女士回答:“我有三个孩子,他们的岁数相乘是 36,岁数相加就等于隔离间屋的门牌号码.”普查员立刻走到隔邻,看了一看,回来说:”我还需要多少资料.”女士回答:“我现在很忙,我最大的孩子正在楼上睡觉.”普查员说:”谢谢,我己知道了 问题: 那三个孩子的岁数是多少?
```
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
```
7. 有两个序列 a,b，大小都为 n,序列元素的值任意整形数，无序;要求:通过交换 a,b 中的元素，使序列 a 元素的和与序列 b 元素的和之间的差最小。
```
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
```
8. 有三顶红帽子和两顶白帽子。将其中的三顶帽子分别戴在 A、B、C 三人头上。这三人每人都只能 看见其他两人头上的帽子，但看不见自己头上戴的帽子，并且也不知道剩余的两顶帽子的颜色。问 A:“你戴的是什么颜色的帽子?” A 回答说:“不知道。” 接着，又以同样的问题问 B。B 想了想之后，也回答说:“不知道。” 最后问 C。C 回答说:“我知道我戴的帽子是什么颜色了。” 当然，C 是 在听了 A、B 的回答之后而作出回答的。请尝试用编程方法解答此问题。
```
def cap_color(is_RED):
    if is_RED:
        return 'red'
    else:
        return 'white'
    
    
def cap_color_possible():
    all_POSSIBLE = [[i, j, k] for i in range(2) for j in range(2) for k in range(2)]
    all_POSSIBLE = np.array(all_POSSIBLE).reshape(8, 3)
    for i in all_POSSIBLE:
        if not ((i[1] == i[2] == 0) or (i[0] == i[2] == 0)) or ((i[0] == i[1] == 1) and (i[2] == 0)):
            print(f'If C see A is wearing {cap_COLOR(i[0])} cap and B is wearing {cap_COLOR(i[1])} cap, he is wearing {cap_COLOR(i[2])} cap.')
```
9. 汉诺塔问题编程解答。 
```
def hanoi_tower(x, y, z, n):
    if n == 1:
        print(f'move disk from {x} to {z}')
    else:
        hanoi_tower(x, z, y, n-1)
        print(f'move disk from {x} to {z}')
        hanoi_tower(y, x, z, n-1)

```
10. 八皇后问题编程解答。
```
def conflict( state, nextX ):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY-i):
            return True
    return False
    
    
def queens(num = 8,state = ()):
    for pos in range(num):
        if not conflict(state,pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num,state+(pos,)):
                    yield (pos,)+result
```
