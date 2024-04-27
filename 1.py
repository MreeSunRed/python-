import math
lst_sides=[3,4,5,6,6,6,4,4,3]
lst_area=[]

for i in range(0,len(lst_sides),3):
    #请补充下面的语句，使其能通过列表切片的方式获得三角形的边长a，b，c
    a,b,c= lst_sides[i:i+3]
    p=(a+b+c)/2
    #下面的语句是用海伦公式计算三角形的面积，请补充完整
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    #请在下面的空白处写语句，利用append函数将计算的s添加进lst_area中
    lst_area.append(s)
for i in lst_area:
    print("{:.2f}".format(i))
