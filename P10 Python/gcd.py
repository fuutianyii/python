# -*- coding: utf-8 -*-

# ���������ֵ����Լ����ŷ������㷨��
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

'''
��չŷ������㷨
���� ax + by = 1�е�x��y�������⣨a��b���ʣ�
'''
def ext_gcd(a, b):
    if b == 0:
        x1 = 1
        y1 = 0
        x = x1
        y = y1
        r = a
        return r, x, y
    else:
        r, x1, y1 = ext_gcd(b, a % b)
        x = y1
        y = x1 - a / b * y1
        return r, x, y
