#请补充下面的函数，使其完成题目要求
def isdiff(n):
   s=str(n)
   for i in s:
       if(s.count(i)>1):
        return False
   return True

n = int(input('请输入一个正整数：'))
if isdiff(n) == 1:
    print('{}的各位数字互不相同'.format(n))
else:
    print('{}中有重复数字'.format(n))