#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
def get_date_list(n):
    if(n<0):
        n = abs(n)
        return date.today()-timedelta(days=n)
    else:
        return date.today()+timedelta(days=n)


def test_data(n):
    #一个列表
    date_list = []
    for i in range(n):
        dt = get_date_list(int('-'+str(i)))
        date_list.append(dt.strftime("%Y-%m-%d"))
