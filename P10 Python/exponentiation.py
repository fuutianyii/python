# -*- coding: utf-8 -*-

'''
���������������Ȼ��Գ��������ȡģ
(base ^ exponent) mod n
'''
def exp_mode(base, exponent, n):
    bin_array = bin(exponent)[2:][::-1]
    r = len(bin_array)
    base_array = []
    
    pre_base = base
    base_array.append(pre_base)
    
    for _ in range(r - 1):
        next_base = (pre_base * pre_base) % n 
        base_array.append(next_base)
        pre_base = next_base
        
    a_w_b = __multi(base_array, bin_array, n)
    return a_w_b % n

def __multi(array, bin_array, n):
    result = 1
    for index in range(len(array)):
        a = array[index]
        if not int(bin_array[index]):
            continue
        result *= a
        result = result % n # �ӿ����˵��ٶ�
    return result
