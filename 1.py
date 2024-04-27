####开始编写isOdd(n)函数，n为奇数时，返回True，否则返回False####

def isOdd(n):
    return True if n%2==1 else False






####函数结束###########################

n = int(input('输入一个整数：'))
if isOdd(n):
    print("{}是奇数".format(n))
else:
    print("{}不是奇数".format(n))