n=int(input("请设置加密位移数："))
dic_convertor={}
for i in range(26):
    ming=ord("a")+i   #ming为键的ASCII编码
    ch=ming+n
    if ch<=122:
        mi=ch             #根据题目要求在注释之前补充句子
    else:
        mi=ch-122+96             #根据题目要求在注释之前补充句子
    dic_convertor[chr(ming)]=chr(mi)

mingwen=input("请输入明文：")
for i in mingwen:
    print(dic_convertor[i],end="")