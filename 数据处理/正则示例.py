import re

#1
example_data="""http://fuutianyii.info.sh https://fuutianyii.info.sh
https://fuutianyii.info.sh
http://fuutianyii.info.sh
"""

rule=re.compile("https?://.*?\.info\.sh")#此处配置规则
re_retrun=re.findall(rule, example_data)
print(re_retrun)
rule=re.compile("https?://.*\.info\.sh")#此处配置规则
re_retrun=re.findall(rule, example_data)
print(re_retrun)
rule=re.compile("https?://(.*?)\.info\.sh")#此处配置规则
re_retrun=re.findall(rule, example_data)
print(re_retrun)
rule=re.compile("https?://(.*)\.info\.sh")#此处配置规则
re_retrun=re.findall(rule, example_data)
print(re_retrun)


example_data="""http://fuutianyii+info+sh https://fuutianyii+info+sh
https://fuutianyii+info+sh
http://fuutianyii+info+sh
"""
rule=re.compile("https?://(.*?)\.info\.sh")#此处配置规则
re_retrun=re.findall(rule, example_data)
print(re_retrun)
rule=re.compile("https?://(.*?).info.sh")#此处配置规则
re_retrun=re.findall(rule, example_data)
print(re_retrun)
rule=re.compile("https://(.*?).info.sh")#此处配置规则
re_retrun=re.findall(rule, example_data)
print(re_retrun)

#正则关键符号    .     匹配除换行符 \n 之外的任何单字符。要匹配 . ，请使用 \. 。
#正则关键符号    ？  设置贪婪符号（*，+）为非贪婪模式,不加则会尽可能少的匹配一行内的表达式（若表达式中没有\n,）详见15，18行或指定前面一个字符匹配一次或两次 详见 30 33



import re
a="199.155.155.256"
rule=re.compile(r"(2[0-55][0-55])|([0-1]?[0-9]{1,2})\.(2[0-55][0-55])|([0-1]?[0-9]{1,2})\.(2[0-55][0-55])|([0-1]?[0-9]{1,2})\.(2[0-55][0-55])|([0-1]?[0-9]{1,2})")
print(re.findall(rule, a))