#!/usr/bin/env python
# coding=utf-8
'''
@Description: 
@Author: Xuannan
@Date: 2020-01-29 19:48:20
@LastEditTime : 2020-01-29 19:52:37
@LastEditors  : Xuannan
'''
from matplotlib import pyplot as plt
import random
x = range(120)
y = [random.randint(20,35) for v in range(120)]
plt.figure(figsize=(150,60),dpi=80)
plt.plot(x,y)
plt.show()
