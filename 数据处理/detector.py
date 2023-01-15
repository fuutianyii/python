'''
Author: fuutianyii
Date: 2023-01-09 14:00:18
LastEditors: fuutianyii
LastEditTime: 2023-01-09 15:08:26
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''

import time


def display_time(func):
    def wrapper(*args):
        name = "function name is {0}".format(func.__name__)
        param = "function param is {0}".format(str(args))
        print(name)
        print(param)
        t1=time.time()
        result=func(*args)
        t2=time.time()
        print(t2-t1)
        return result
    return wrapper



# @display_time
# def devide_exactly_define(num):
#     count=0
#     for i in range(1,500):
#         if ((i%num)==0):
#             count+=1
#     return count

@display_time
def devide_exactly(num,max):
    count=0
    for i in range(1,max):
        if ((i%num)==0):
            count+=1
    return count
            
# devide_exactly_define(2)
devide_exactly(2,10000)




arg=(2,10000)

devide_exactly(*arg)