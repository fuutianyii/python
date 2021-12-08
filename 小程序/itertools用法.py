import itertools
for i in itertools.count(start=1,step=1): #start 从...开始 step 步数
    pass
a = ['1','2','3','4','5','6']
for i in itertools.cycle(a): #无限迭代a
    pass
for i in itertools.repeat(a,5): #输出列表a 5表示次数 ,若不输出则无限输出
    pass
d = {'a': 1, 'b': 2, 'c': 3}
c = itertools.accumulate(d) #返回列表,字典,元组d累加 A AB AC
for i in c:
    print(i)
s=d.values() #返回一个字典d累加 A AB AC
print(s)
for i in itertools.product(a,repeat=2): #a 列表 生成元组i为a的列表的组合,repeat为重复列表a 2次
    pass
##### Iterable：
#所谓可迭代数据流，即能直接参与for循环的数据类型：Iterable
#一类是集合数据类型，如list / tuple / dict / set / str /等;
#一类是generator，包括生成器和带yield的generator function。