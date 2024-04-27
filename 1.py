#请补充下面的句子，创建一个名为dic_student的空字典
dic_student={}
for i in range(1,6):
    name=input()
    age=eval(input())
    #请在下面的空白处写句子，将用户输入的name当成dic_student的键，age当成值，
    dic_student[name]=age
for k,v in dic_student.items():
    #请补充下面的句子，按要求输出字典中的数据
    print("{:<6}%d岁".format(k)%v)
