myDict={'方糖':99,'x1':499,'魔盒':399,'曲奇':299}
#请补充下面的句子，用items方法遍历字典的键和值
for k,v in myDict.items():
    print(k+'\t…………\t'+str(v))
lst=[]
#请补充下面的句子，用values方法遍历字典的值
for v in myDict.values():
    lst.append(v)
print('所有产品的平均价为：{}'.format(sum(lst)/len(lst)))
newlst=[(v,k) for k,v in myDict.items()]
#请在下面空白处写句子，用sort方法对newlst进行升序排列
newlst.sort()
print('价格最高的产品是：{}'.format(newlst[-1][1]))
