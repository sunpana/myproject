#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
斐波拉契数列的几种写法
'''

def fab_0(m):
    '''直接打印数列'''
    n , a , b = 0 , 0 , 1
    while n < m:
        print b
        a , b = b , a + b
        n = n + 1

def fab_1(m):
    '''返回一个数列列表'''
    n , a , b = 0 , 0 , 1
    fab_list = []
    while n < m:
        fab_list.append(b)
        a , b = b , a + b
        n = n + 1
    return fab_list

def fab_2(m):
    '''通过iterable对象迭代'''
    pass

def fab_3(m):
    '''返回对象迭代值'''
    n , a , b = 0 , 0 , 1
    while n < m:
        yield b
        a , b = b , a + b
        n = n + 1

if __name__ == "__main__":
    #fab_0(10)
    #print fab_1(10)
    a = fab_3(10)
    for i in a:
        print i

