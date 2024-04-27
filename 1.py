import random


# 请补充下面的函数，使其完成题目的要求
def delSame(ls):
    t = []
    for p in ls:
        if not p in t:
            t.append(p)

    return t


data = [1, 2, 3, 4, 5, 2, 1, 4, 5, 3, 8, 8, 9]

print(delSame(data))
