import random,string
from optparse import OptionParser
o= OptionParser()
o.add_option('--max',type = "int" ,dest='max')
o.add_option("--min",type = 'int' ,dest="min")
o.add_option("--len",type = 'int' ,dest="len")
#optParser.parse_args() 剖析并返回一个字典和列表，
#字典中的关键字是我们所有的add_option()函数中的dest参数值，
#而对应的value值，是add_option()函数中的default的参数或者是
#由用户传入optParser.parse_args()的参数
#fakeArgs =['-A',10,'-I',5]
op,ar= o.parse_args()
len=op.len
max=op.max
min=op.min
m=''
for i in range(0,len):
    m=''
    for r in range(0,random.randint(min,max)):
        m+=random.choice(string.ascii_letters+string.digits)
    print(m)
