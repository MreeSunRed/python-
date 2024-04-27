###请定义函数LeapYear(year)，闰年返回True，否则返回False###
def isLeapYear(year):
    if year%400==0 or year%4==0 and not year%100==0:
        return True
    else :
        return False





#####函数定义结束########################################


count = 0
for n in range(1900, 2021):
    if isLeapYear(n) is True:
        print(n, end='\t')
        count += 1
        if count % 5 == 0:
            print()
