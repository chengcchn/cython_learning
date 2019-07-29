#!/usr/bin/env python
# coding: utf-8

"""
Name    : cython_test.py
Author  : Charlie Chen
Contect : chengcchn@gmail.com
Time    : 2019/7/29 15:15
Desc    :
"""

import datetime
import pyximport
pyximport.install()
import fibonacci_c

def fibonacci(n):
    if n < 0:
        print("1st fibonacci number = 0")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

start = datetime.datetime.now()
print(fibonacci_c.fibonacci_c(39))
end = datetime.datetime.now()
print("fibonacci_c escaped: " + str((end-start).seconds) + "s")


start = datetime.datetime.now()
print(fibonacci(39))
end = datetime.datetime.now()
print("fibonacci escaped: " + str((end-start).seconds) + "s")
