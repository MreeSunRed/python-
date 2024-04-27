
print(ord("倪"))
print(chr(20522))
n=1
while 1:
    #请补充下面的if语句
    if n%2==1 and n%3==0 and n%4==1 and n%5==4 and n%6==3 and n%7==0 and n%8==1 and n%9==0:
        print("这个盒子里一共有{}个糖果".format(n))
        break
    else:
        n=n+1

